import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     result = -1
#     for i in range(1, 1000001):
#         if N == i ** 3:
#             result = i
#             break
#     print(f'#{tc} {result}')

# 모든 범위 탐색하면 오래걸릴거같으니 (329ms)
# 이분탐색 ㄱㄱ~ (168ms)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    start, end = 1, N
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if N == mid ** 3:
            result = mid
            break
        elif N < mid ** 3:
            end = mid - 1
        else:
            start = mid + 1
    print(f'#{tc} {result}')

