import sys
sys.stdin = open('input.txt')

def DFS(adjl):
    visited = [0] * (V+1)
    stack = []
    result = []
    visited[v2] = 1


for tc in range(1, 11):
    V, E = map(int, input().split())
    adjl = [[] for _ in range(V)]
    arr = list(map(int, input().split))
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjl[v1].append(v2)
    print(f'#{tc} {DFS(adjl)}')
