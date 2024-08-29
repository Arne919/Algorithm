import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    ddr = [-1,-1,1,1]
    ddc = [-1,1,-1,1]
    max_kill = 0
    for i in range(n):
        for j in range(n):
            cnt1 = arr[i][j]
            cnt2 = arr[i][j]
            for k in range(4):
                for l in range(1, m):
                    nr = i + dr[k] * l
                    nc = j + dc[k] * l
                    nnr = i + ddr[k] * l
                    nnc = j + ddc[k] * l
                    if 0 <= nr < n and 0 <= nc < n:
                        cnt1 += arr[nr][nc]
                    if 0 <= nnr < n and 0 <= nnc < n:
                        cnt2 += arr[nnr][nnc]
            if max_kill < cnt1:
                max_kill = cnt1
            if max_kill < cnt2:
                max_kill = cnt2
    print(f'#{tc} {max_kill}')
