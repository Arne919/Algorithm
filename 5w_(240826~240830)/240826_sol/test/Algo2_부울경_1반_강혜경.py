# import sys
# sys.stdin = open('algo1_sample_in.txt')

def DFS(start):
    pass

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = N*100

    for i in range(N):
        start = arr[0][i]
        sum1 = DFS(start)