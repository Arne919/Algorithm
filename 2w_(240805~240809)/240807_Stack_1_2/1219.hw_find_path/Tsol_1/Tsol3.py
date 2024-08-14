import sys; sys.stdin = open('input.txt')
# *****길찾기_재귀_인접*****

def DFS(v):
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            DFS(w)

for tc in range(1, 11):
    tc_num, E = map(int, input().split())   # tc 번호, 간선수
    arr = list(map(int, input().split()))


    # 인접 리스트
    G = [[] for _ in range(100)]    # 정점 번호 0 ~ 99
    for i in range(0, E*2, 2):
        u, v = arr[i], arr[i+1]
        G[u].append(v)              # 유향 그래프

    visited = [0] * 100

    DFS(G, 0)

    print(f'#{tc} {visited[99]}')
