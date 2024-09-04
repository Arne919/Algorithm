import sys
sys.stdin = open('input.txt')

def dfs(lev):
    global result
    if lev == cnt:
        result = max(result, int(''.join(map(str, num))))
        return

    for i in range(L - 1):
        for j in range(i + 1, L):
            num[i], num[j] = num[j], num[i]

            change = int(''.join(map(str, num)))
            if (lev, change) not in visited:
                dfs(lev + 1)
                visited.append((lev, change))
            num[i], num[j] = num[j], num[i]


T = int(input())
for test_case in range(1, T + 1):
    N, cnt = map(int, input().split())
    num = list(map(int, str(N)))

    L = len(num)
    result = 0
    visited = []
    dfs(0)
    print(f'#{test_case} {result}')