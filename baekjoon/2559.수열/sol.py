import sys
sys.stdin = open('input.txt')

result = []
N, K = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(N - K + 1):
    result.append(sum(arr[i:i+K]))
    
print(max(result))