import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))
    result = B

    for i in range(2**N):
        top = 0
        for j in range(N):
            if i & (1<<j):
                top += data[j]
        if top >= B and result >= top - B:
            result = top - B
    print(f'#{tc} {result}')