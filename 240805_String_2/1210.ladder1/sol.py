import sys
sys.stdin = open('input.txt')


for _ in range(10):
    tc = input()
    arr = [input().split() for _ in range(100)]
    c = 0
    r = N - 1

    for i in range(100):
        if arr[r][i] == '2':
            c = i
            break

    dr = [0,0,-1]
    dc = [-1,1,0]
    while r > 0:
        for k in range(3):
            nr = r +dr[k]
