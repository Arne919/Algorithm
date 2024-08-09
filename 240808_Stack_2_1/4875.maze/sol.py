import sys
sys.stdin = open('input.txt')

def DFS(row, col):
    global result

    if arr[row][col] == 3:      # 목표지점 도달시 종료
        result = 1
        return

    visited[row][col] = 1
    dr = [0, 1, 0, -1]  # 우, 하, 좌, 상
    dc = [1, 0, -1, 0]

    for k in range(4):
        nr = row + dr[k]
        nc = col + dc[k]
        # 범위 안에 있고 방문하지 않았으며, 벽이 아닌곳
        if 0 <= nr < N and 0<=nc<N and visited[nr][nc] == 0 and arr[nr][nc] != 1:
            DFS(nr, nc) # 재귀호출
            # DFS 호출 후 현재 방향에서 모든 가능한 경로를 탐색했으므로,
            # 다음 방향으로 진행하거나 현재 함수에서 돌아감

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    for r in range(N):          # 시작지점 찾기
        for c in range(N):
            if arr[r][c] == 2:
                row = r
                col = c
    DFS(row, col)               # DFS함수 호출

    print(f'#{tc} {result}')






