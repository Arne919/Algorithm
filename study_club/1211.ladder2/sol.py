import sys
sys.stdin = open('input.txt')

N = 100
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 0, -1]  # 좌, 우, 상
    dc = [-1, 1, 0]
    min_cnt = 100*100
    result_col = -1
    for start_col in range(N):
        if arr[N-1][start_col] == 1:
            row, col = N-1, start_col
            cnt = 0

            while row > 0:
                for k in range(3):
                    nr = row + dr[k]
                    nc = col + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                        arr[row][col] = '0'
                        row, col = nr, nc
                        cnt += 1
                        break
            if min_cnt > cnt:
                min_cnt = cnt
                result_col = start_col
    print(f'#{tc} {result_col}')


