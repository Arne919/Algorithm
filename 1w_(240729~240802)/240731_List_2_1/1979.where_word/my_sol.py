import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    new_arr = [[0] * (N + 2)]
    for r in arr:
        new_arr.append([0] + r + [0])
    new_arr.append([0] * (N + 2))
    count = 0

    for i in range(1, N+1):
        for j in range(1, N-k+2):
            if sum(new_arr[i][j:j+k])==k and new_arr[i][j-1]==0 and new_arr[i][j+k]==0:
                count+=1
    for j in range(1, N + 1):
        for i in range(1, N - k + 2):
            if sum(new_arr[i + l][j] for l in range(k)) == k and new_arr[i - 1][j] == 0 and new_arr[i + k][j] == 0:
                count += 1

    print(f'#{tc} {count}')