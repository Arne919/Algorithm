import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            live_fly = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    fly += arr[k][l]
                    if i+1 <= k <= i+M-2 and j+1 <= l <= j+M-2:
                        live_fly += arr[k][l]

            if result < (fly-live_fly):
                result = (fly-live_fly)
    print(f'#{tc} {result}')
