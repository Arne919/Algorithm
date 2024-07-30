import sys
sys.stdin = open('input.txt')


def my_len(lst):
    cnt = 0
    for i in lst:
        cnt += 1

    return cnt


T = 10
for tc in range(1, T+1):
    D = int(input()) # 최대 덤프 횟수
    target = list(map(int, input().split()))  # 평탄화 장소

    # 상자의 높이를 저장할 배열 생성 (카운팅 정렬의 COUNT 리스트 활용)
    h_count = [0] * 101

    # 최대와 최소 높이를 저장하기 위한 변수
    # 초기 값은 첫 번째 값을 기준
    min_value = target[0]
    max_value = target[0]
    for idx in range(my_len(target)):
        value = target[idx]
        # 상자 높이의 갯수
        h_count[value] += 1
        # 최대 최소 갱신
        if min_value > value:
            min_value = value
        if max_value < value:
            max_value = value

    for j in range(D):   # 덤프 횟수 만큼 반복

        # 덤프로 인한 상자 갯수 수정
        # 최대 상자는 1개 감소 (상자를 옮기기 위해 1개 뺌)
        # 그로 인해 최대 상자 높이 - 1 의 상자 갯수가 1증가 
        h_count[max_value] -= 1
        h_count[max_value-1] += 1

        # 상자 낮은 것의 갯수 수정
        # 최소 상자 1개 감소 (상자가 1개 옮겨졌기 때문)
        # 그로 인해 최소 상자 + 1 높이의 상자 갯수가 1 증가
        h_count[min_value] -= 1
        h_count[min_value+1] += 1

        # 더 이상 옮길 최대 상자의 높이가 없다면
        if h_count[max_value] == 0:     # 최대 상자가 없는 경우 그 다음 최대 상자로 갱신
            max_value -= 1
            
        if h_count[min_value] == 0:     # 최소 상자가 없는 경우 그 다음 최소 상자로 갱신
            min_value += 1

    # 모든 덤프를 하고 나면 최대 값 - 최소 값 차이 출력
    print(f'#{tc} {max_value - min_value}')