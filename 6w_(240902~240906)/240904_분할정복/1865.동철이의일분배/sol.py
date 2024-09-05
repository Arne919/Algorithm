import sys
sys.stdin = open('input.txt')

def dfs(n, items, total):
    global result
    if total <= result:
        return
    if n == N:
        result = max(result, total)
        return
    for i in range(N):
        if i not in items:
            items.append(i)
            dfs(n+1, items, total*(arr[n][i]/100))
            items.pop()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    dfs(0, [], 1)
    # result1 = round(result*100,6)
    print(f'#{tc} {result*100:6f}')