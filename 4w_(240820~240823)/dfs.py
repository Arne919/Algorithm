import sys
sys.stdin = open('dfs_input.txt')

def DFS(s, V):              # s 시작정점, v 정점개수
    visited = [0] * (V+1) # 방문한 정점을 표시
    stack = []              # 스택 생성
    visited[s] = 1          # 시작정점 방문표시
    print(s)
    v = s
    while True:
        for w in adjl[v]:       # v에 인접하고, 방문안한 w가 있으면
            if visited[w]==0:
                stack.append(v) # push(v) 현재 정점을 push하고
                v=w             # w에 방문
                print(v)
                visited[w] = 1  # w애 방문표시
                break           # v부터 다시 탐색 (for w에 대한 break)
        else:               # 남은 인접정점이 없어서 break가 걸리지 않은 경우
            if stack:       # 이전 갈림길을 스택에서 꺼내서... if TOP -> -1
                v = stack.pop()
            else:
                break       # while true 에 대한 break



T = int(input())
for tc in range(1, T+1):
    V, e = map(int, input().split())
    adjl = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(e):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjl[v1].append(v2)
        adjl[v2].append(v1)
    # print(adjl)
    DFS(1, V)