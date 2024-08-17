import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    #선택
    for i in range(N - 1):
        max_idx = i
        for j in range(i + 1, N):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    # result = sum(arr[:K])
    for i in range(K):
        result += arr[i]

    print(f'#{tc} {result}')