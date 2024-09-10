import sys
sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = 1  # 방문 표시
    for nxt in graph[v]:    # 정점에서 연결된 정점들 순회
        if visited[nxt]:    # 방문하지 않은 정점들 선택
            continue
        dfs(nxt)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]    # 1 ~ N번
    for i in range(M):      # 무방향(쌍방) 그래프 연결 상태
        v1 = arr[i*2]
        v2 = arr[i*2+1]
        graph[v1].append(v2)
        graph[v2].append(v1)
    visited = [0 for _ in range(N+1)]
    cnt = 0
    for i in range(1, N+1):
        if visited[i]:  # 방문확인
            continue
        dfs(i)          # 연결 요소 모두 방문 표시
        cnt += 1        # 연결 요소 개수 +1
    print(f'#{tc} {cnt}')