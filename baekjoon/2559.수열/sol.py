import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

result = []
result.append(sum(arr[:K]))

for i in range(N-K):
    result.append(result[i] - arr[i] + arr[K+i])

print(max(result))

# ㅅ_ㅂ 시간초과데스
# result = []
# N, K = map(int, input().split())
# arr = list(map(int, input().split()))

# for i in range(N - K + 1):
#     result.append(sum(arr[i:i+K]))

# print(max(result))