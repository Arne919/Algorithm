import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input() for _ in range(N))
    dir = [(1, 0), (0, 1), (1, -1), (1, 1)]
    result = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    row, col = i, j
                    cnt = 0
                    while 0 <= row < N and 0 <= col < N and arr[row][col] == 'o':
                        cnt += 1
                        dir_r, dir_c = dir[k]
                        row += dir_r
                        col += dir_c
                        if cnt >= 5:
                            result = 'YES'
    print(f'#{tc} {result}')