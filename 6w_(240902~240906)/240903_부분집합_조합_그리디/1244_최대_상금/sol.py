import sys
sys.stdin = open('input.txt')

def dfs(lev):
    global result
    if lev == cnt:
        result = max(result, int(''.join(num)))
        return
    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]
            chk = int(''.join(num))
            if (lev, chk) not in visited:
                dfs(lev+1)
                visited.append((lev,chk))
            lst[i], lst[j] = lst[j], lst[i] # 반드시 원상복구


T = int(input())
for tc in range(1, T+1):
    N, cnt = map(int, input().split())
    num = list(str(N))
    L = len(num)
    lst, visited = [], []
    result = 0
    for i in num:
        lst.append(i)
    dfs(0)
    print(f'#{tc} {result}')