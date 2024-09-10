import sys
sys.stdin = open('input.txt')

def dfs(n):
    global result
    # 마지막행까지 퀸을 다 놓았는지
    if n == N:
        result += 1
        return
    for i in range(N):
        if v1[i] == v2[n+i] == v3[n-i] == 0:    # 같은열, 우상대각, 좌상대각 퀸x
            # 방문표시 체크
            v1[i] = 1
            v2[n + i] = 1
            v3[n - i] = 1
            dfs(n+1)    # 다음행으로 이동
            # 방문표시 해제(백트래킹)
            v1[i] = 0
            v2[n + i] = 0
            v3[n - i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)] # NxN 체스판
    v1 = [0]*N      # 위쪽
    v2 = [0]*(N*2)  # 오른쪽 위 대각
    v3 = [0]*(N*2)  # 왼쪽 위 대각
    result = 0
    dfs(0)
    print(f'#{tc} {result}')