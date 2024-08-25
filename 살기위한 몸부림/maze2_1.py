import sys
sys.stdin = open('maze2_input.txt')

def DFS(start, visited):
    global N, arr
    row, col = start[0], start[1]
    
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    stack = [(row, col)]
    visited[row][col]=1

    while stack:
        row, col = stack.pop()

        for k in range(4):
            nr=row+dr[k]
            nc=col+dc[k]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0:
                if arr[nr][nc] ==3:
                    return 1
                elif arr[nr][nc]==0:
                    stack.append((nr, nc))
                    visited[nr][nc]=1
                
    return 0

for tc in range(1, 11):
    T = int(input())
    N = 100
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] *N for _ in range(N)]
    start = []
    
    for r in range(N):          # 시작지점 찾기
        for c in range(N):
            if arr[r][c] == 2:
                start.append(r)
                start.append(c)
                  # DFS함수 호출

    print(f'#{tc} {DFS(start, visited)}')