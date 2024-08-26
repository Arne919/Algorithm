import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    current = 0             # 첨위치
    while arr[current]:     # 먹이가 있으면
        current += K        # K만큼 이동
        if current >= N-1:  # 마지막에 도착했을때(탈출조건)
            result = N
    result = current+1      # 없다면 그 위치 반환

    print(f'#{tc} {result}')
