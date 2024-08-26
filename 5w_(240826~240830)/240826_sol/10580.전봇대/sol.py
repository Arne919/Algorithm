import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1) :
    N = int(input())
    data = []
    result = 0

    for _ in range(N):
        a, b = map(int, input().split())
        if data:
            for da, db in data:
                if (a < da and b > db) or (a > da and b < db) :
                    result += 1
        data.append((a, b))
    print(f'#{tc} {result}')