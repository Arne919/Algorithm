import sys
sys.stdin = open('input.txt')

T = int(input())                            # 테스트케이스 수 T

for test_case in range(1, T + 1):           # 테스트케이스 반복
    N = int(input())                        # 양수의 개수 N
    arr = list(map(int, input().split()))   # N개의 양수

    max_value = 0                           # 1<=양수<=10 범위이기때문에
    min_value = 11                          # max는 0, min은 11로 초기화
    max_position = 0                        # 최댓값,최솟값의 위치 0으로 초기화
    min_position = 0

    for i in range(N):                      # 양수의 개수 만큼 반복
        if arr[i] > max_value:              # i번째 양수가 최대값일때
            max_value = arr[i]              # 최댓값 갱신
            max_position = i                # 최댓값위치 갱신
        elif arr[i] == max_value:           # i번째 양수가 최댓값과 같을때
            max_position = i                # 최댓값위치 갱신 (마지막으로 나오는 위치)
        if arr[i] < min_value:              # i번째 양수가 최솟값일때 (값같을때는 갱신할필요x)
            min_value = arr[i]              # 최솟값 갱신
            min_position = i                # 최솟값위치 갱신

    result = abs(max_position - min_position) # 최댓값위치-최솟값위치의 절대값

    print(f'#{test_case} {result}')