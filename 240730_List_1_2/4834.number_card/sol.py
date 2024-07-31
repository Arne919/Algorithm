import sys
sys.stdin = open('input.txt')

T = int(input())                            # 테스트케이스 수 T

for test_case in range(1, T + 1):           # 테스트케이스 반복
    N = int(input())                        # 입력받은 카드 장수 N
    arr = list(map(int, input()))           # 입력받은 카드 숫자 list
    count = [0] * 10                        # 0~9 숫자 횟수를 저장할 리스트 초기화
    for num in arr:                         # 각 카드 순회해서 횟수 계산
        count[num] += 1
    
    max_count = 0                           # 최대 횟수
    max_card = 0                            # 최대 횟수가 나온 카드 숫자

    for i in range(10):                     # 0~9숫자 횟수 리스트 반복
        if count[i] > max_count:            # 숫자의 최대횟수, 그숫자 갱신
            max_card = i
            max_count = count[i]
        elif count[i] == max_count:         # 카드 장수가 같을 때
            if i > max_card:                # 적힌 숫자가 큰 쪽 출력
                max_card = i

    print(f'#{test_case} {max_card} {max_count}')