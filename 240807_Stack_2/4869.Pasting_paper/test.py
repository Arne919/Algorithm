import sys
sys.stdin = open('input.txt')

def count_ways(N):
    dp = [0] * (N + 1)
    dp[0] = 1  # 아무것도 없는 상태도 한 가지 경우의 수
    dp[10] = 1  # 10x20 한 장 놓는 경우
    
    for i in range(20, N + 1, 10):
        dp[i] = dp[i - 10] + 2 * dp[i - 20]
    
    return dp[N]

# 입력 받기
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    result = count_ways(N)
    print(f'#{t} {result}')
