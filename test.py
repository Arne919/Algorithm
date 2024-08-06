import sys
sys.stdin = open('input.txt')

T = 10
N = 100
for tc in range(1, T + 1):
    _ = input()
    arr = [input().split() for _ in range(N)]
    col = 0
    row = N-1
    min_count = 100*100
    for idx in range(N):
        count = 0
        if arr[row][idx] == '1':
            col=idx

            dr = [0, 0, -1]
            dc = [-1, 1, 0]
            while row > 0:
                for k in range(3):
                    nr = row +dr[k]
                    nc = col +dc[k]
                    if 0<=nr<N and 0<=nc<N:
                        if arr[nr][nc]=='1':
                            arr[row][col]='0' # 변경해버리면 다음꺼 출발 할때 초기화해야는데
                            count += 1
                            row=nr
                            col=nc
                            break

    if min_count > count:
        min_count = count
        min_col = col
    elif min_count == count:
        if min_col > col:
            min_col = col
    print(f'#{tc} {min_col}')
