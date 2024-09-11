import sys
sys.stdin = open('input.txt')

def prim(r, V):
    MST = [0] * (V+1)       # 정점 포함 여부
    key = [1e9] * (V+1)     # 가중치의 최대값 이상으로 초기화, key[v]는 v가 MST에 속한 정점과 연결될 때의 가중치
    key[r] = 0              # 시작 정점의 key 0으로 초기화
    for _ in range(V):      # V+1개의 정점 중 V개 선택
        u, w = 0, 1e9
        # MST에 포함되지 않은 정점 중, key가 최소인 u 찾기
        for i in range(V+1):
            if MST[i]==0 and key[i] < w:
                u, w = i, key[i]
        MST[u] = 1          # 정점 u를 MST에 포함
        # u에 인접한 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v]==0 and graph[u][v] > 0:
                # u를 통해 MST에 포함되는 비용과 기존 비용을 비교, 갱신
                key[v] = min(key[v], graph[u][v])
    # MST 가중치의 합을 return
    return sum(key)

for tc in range(int(input())):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        u, v, weight = map(int, input().split())
        graph[u][v] = weight
        graph[v][u] = weight

    # for line in G:
    #     print(line)
    print(f'#{tc+1}', prim(0, V))