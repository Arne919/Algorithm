N = 5
arr = [[0] * N for _ in range(N)]


for r in range(N):
    for c in range(0, r + 1):
        arr[r][c] = 1

for lst in arr:
    print(*lst)