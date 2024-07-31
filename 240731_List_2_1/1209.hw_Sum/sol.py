import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = 100                         # 리스트의 크기 NxN

    test_case = int(input())        # 테스트 케이스 번호

    # arr = []
    # for i in range(N):
    #     line = list(map(int, input().split()))
    #     arr.append(line)
    #     print(arr)
    arr = [list(map(int, input().split())) for i in range(N)]


    # 행 탐색
    # total = 0                     # 이곳에 초기화를 하면 (행렬의 모든 값의 합)
    max_value = 0
    for r in range(N):
        # 행 별로 합계를 확인하기 위해 이곳에서 초기화
        total = 0                   # total 은 더해야 하는 범위가 있기 때문에 초기화가 필요
        for c in range(N):
            total += arr[r][c]
        # 방금 합한 행의 값이 과연 최대 값인지 확인
        if max_value < total:
            max_value = total       # 최대값 갱신
    # print(max_value)              # 행의 합 중 가장 큰 값이 저장 됨


    # max_value = 0                 # 초기화를 하게 되면 행의 합 중에서 최대 값과 비교 할 수 없게 됨
    # (행의 최대 값을 따로 저장해야 함 => 굳이 저장해서 확인할 필요가 있을까? 생각해볼 수 있음)
    # 열 탐색
    for c in range(N):
        total = 0
        for r in range(N):
            total += arr[r][c]
        if max_value < total:
            max_value = total
    # print(max_value)              # 행의 합, 열의 합 중 가장 큰 값이 저장 됨


    # 대각선 합 (좌측 상단에서 우측 하단으로)
    total = 0
    for i in range(N):
        total += arr[i][i]
    if max_value < total:
        max_value = total


    # 역 대각선 합 (우측 상단에서 좌측 하단으로)
    total = 0
    for i in range(N):
        total += arr[i][99-i]
    if max_value < total:
        max_value = total
    # print(max_value)              # 행의 합, 열의 합, 대각선들의 합 중 가장 큰 값이 저장 됨
    print(f'#{tc} {max_value}')