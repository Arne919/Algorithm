import sys
sys.stdin = open('miro_way.txt')

def dfs(x, y):
    visited = [[0]*N for _ in range(N)]
    stack = [(x, y)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    while stack:
        x, y = stack.pop(0)
        if maze[x][y] == 0 or maze[x][y] == 2:
            maze[x][y] = 1
            for k in range(4):
                nr = x + dr[k]
                nc = y + dc[k]
                if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
                    if maze[nr][nc] == 3:
                        return visited[x][y]
                    elif maze[nr][nc] == 0:
                        stack.append((nr, nc))
                        visited[nr][nc] = visited[x][y] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                row, col = r, c

    print(f'#{tc} {dfs(row, col)}')