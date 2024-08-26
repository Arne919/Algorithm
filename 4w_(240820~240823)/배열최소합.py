import sys
sys.stdin = open('4881_배열최소합_input.t')

def backtrack(x, current_sum):
    global min_sum

    if current_sum >= min_sum:
        return
    if x == N:
        if min_sum > current_sum:
            min_sum = current_sum
        return
    for i in range(N):
        if visited_col[i]==0:
            visited_col[i] = 1
            backtrack(x+1, current_sum+arr[x][i])
            visited_col[i]=0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = N*N*10  #최소합
    visited_col = [0] *N
    backtrack(x=0, current_sum = 0)
    print(f'#{tc} {min_sum}')