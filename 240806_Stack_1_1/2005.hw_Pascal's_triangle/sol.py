import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [[0] * N for _ in range(N)]
    print(f'#{tc}')
    for r in range(N):
        for c in range(r+1):
            if c == 0 or c == r:
                arr[r][c] = 1
            else:
                arr[r][c] = arr[r-1][c-1] + arr[r-1][c]
            print(arr[r][c], end =' ')
        print()