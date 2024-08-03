import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_arr = list(map(int, input().split()))
    M_arr = list(map(int, input().split()))
 
    total = 0
    if N <= M:
        for j in range(M - N + 1):
            num = 0
            for i in range(N):
                num += N_arr[i] * M_arr[i+j]
            if total < num:
                total = num
    elif N > M:
        for i in range(N-M+1):
            num=0
            for j in range(M):
                num += N_arr[i+j] * M_arr[j]
            if total < num:
                total = num
    print(f'#{tc} {total}')