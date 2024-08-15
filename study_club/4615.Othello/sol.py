import sys
sys.stdin = open('input.txt')

dir = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]    # 상하좌우대각

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    # print(arr)

    arr[N//2-1][N//2],arr[N//2][N//2-1],arr[N//2-1][N//2-1],arr[N//2][N//2] = 1,1,2,2 # 흑흑백백/초기값2x2
    # print(arr)

    for i in range(M):
        r, c, color = map(int, input().split())
        r, c = r-1, c-1
        arr[r][c] = color   # 돌 놓기
        for i in range(8):
            dr, dc = dir[i]
            nr = r + dr
            nc = c + dc
            data = []       # 뒤집을 돌
            # 범위안에있고, 빈칸아니고, 다른돌일때 ㄱㄱ
            while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0 and arr[nr][nc] != color:
                data.append((nr, nc))   # 뒤집을돌 추가
                nr += dr
                nc += dc
            # 범위안에있고, 같은돌이면
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == color:
                for jr, jc in data:     # 돌뒤집기
                    arr[jr][jc] = color
        
    # 흑돌,백돌 개수 계산
    black, white = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')
