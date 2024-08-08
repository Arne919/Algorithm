import sys; sys.stdin = open('input.txt')
# ====================================
# - 인접 정점 정보를 인접 리스트로 저장
# - 스택을 사용한 반복 구조
# *****길찾기_반복_인접*****
# ====================================

def DFS(G, v):
    S = []
    visited = [0] * 100
    # 시작점 방문
    visited[v] = 1
    S.append(v)

    while True:
        # v 에서 w 를 방문
        for w in G[v]:
            if not visited[w]:
                visited[w] = 1
                S.append(v)
                v = w
                break
        else:
            if not S: break
            v = S.pop()

    return visited[99]


for tc in range(1, 11):
    tc_num, E = map(int, input().split())   # tc 번호, 간선수
    arr = list(map(int, input().split()))


    # 인접 리스트
    G = [[] for _ in range(100)]    # 정점 번호 0 ~ 99
    for i in range(0, E*2, 2):
        u, v = arr[i], arr[i+1]
        G[u].append(v)              # 유향 그래프



    ans = DFS(G, 0)

    print(f'#{tc} {ans}')
