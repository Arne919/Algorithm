import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    # +
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    # x
    ddr = [-1,1,-1,1]
    ddc = [-1,1,1,-1]

    result = 0
    for i in range(N):
        for j in range(N):
            cnt1 = arr[i][j]
            cnt2 = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    nr = i + dr[k] * l
                    nc = j + dc[k] * l
                    nnr = i + ddr[k] * l
                    nnc = j + ddc[k] * l
                    if 0<=nr<N and 0<=nc<N:
                        cnt1 += arr[nr][nc]
                    if 0<=nnr<N and 0<=nnc<N:
                        cnt2 += arr[nnr][nnc]
            if result < cnt1:
                result = cnt1
            if result < cnt2:
                result = cnt2

    print(f'#{tc} {result}')