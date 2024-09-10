import sys
sys.stdin = open('input.txt')

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]

max_kill = 0

for i in range(N):
    for j in range(N):
        kill = 0
        for l in range(1, K + 1):
            for a in range(4):
                nr = i + dr[a] * l
                nc = j + dc[a] * l
                if 0 <= nr < N and 0 <= nc < N:
                    kill += area[nr][nc]

        if max_kill < kill:
            max_kill = kill
print(max_kill)