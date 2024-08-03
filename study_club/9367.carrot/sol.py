import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    count = 1
    max_count = 1
    for i in range(N-1):
        if C[i] < C[i+1]:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 1
    print(f'#{tc} {max_count}')