import sys
sys.stdin = open('input.txt')


# DFS인데 백트래킹가능 (문어쓰앵님..모르겠워요.....)
def dfs(n, alst, blst):
    global result
    if n == N:
        if len(alst) == M:  # a음식에 선택된 재료개수가 절반일 경우
            asum = bsum = 0 # 음식맛의 합 구하기
            for i in range(M):
                for j in range(M):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            result = min(result, abs(asum-bsum))
        return
    dfs(n+1, alst+[n], blst)# a음식에 추가
    dfs(n+1, alst, blst+[n])# a음식에 추가

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = N//2
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 20000*N*N
    dfs(0, [], [])  # n, alst, blst
    print(f'#{tc} {result}')