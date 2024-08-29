import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 0, 1, -1, 1, -1, 0, 1]
    dc = [-1, -1, -1, 0, 0, 1, 1, 1]

    result = 0
    for i in range(N):
        for j in range(M):
            count = 0
            for k in range(8):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < M and area[nr][nc] < area[i][j]:
                    count += 1
            if count >= 4:
                result += 1
    print(f'#{tc} {result}')