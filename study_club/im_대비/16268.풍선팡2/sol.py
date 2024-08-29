import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 0, 1, 0, -1]
    dc = [0, 1, 0, -1, 0]

    max_total = 0
    for i in range(N):
        for j in range(M):
            total = 0
            for k in range(5):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc <M:
                    total += balloon[nr][nc]
            if max_total < total:
                max_total = total
    print(f'#{tc} {max_total}')
