import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                count += arr[i][j]
            elif N-1-i == j:
                count += arr[i][j]
    print(f'#{tc} {count}')
