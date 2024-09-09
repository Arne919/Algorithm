import sys
sys.stdin = open('input.txt')



def check(r, c, num):
    global result
    # 구하려는 최솟값보다 큰값이면 더 실행 x
    if result < num:
        return
    # 도착지점에 도착했을때 지나온길의 합이 더 적으면 최소합 갱신
    if r == N-1 and c == N-1:
        if result > num:
            result = num
        return
    # 방향백터(우, 하) 이동
    dr = [0, 1]
    dc = [1, 0]
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N: # 범위내일때
            check(nr, nc, num+arr[nr][nc])  #이동



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10*2*N
    check(0, 0, arr[0][0])
    print(f'#{tc} {result}')