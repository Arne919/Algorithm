import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M  = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(M):
        arr.append(arr[0])
        arr.pop(0)

    print(f'#{tc} {arr[0]}')
    # print(f'#{tc} {arr[M%N]}')