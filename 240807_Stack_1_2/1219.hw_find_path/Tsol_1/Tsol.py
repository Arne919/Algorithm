import sys; sys.stdin = open('input.txt')
# ====================================
# - 인접 정점 정보를 1차 배열 2개에 저장
# - 스택을 사용한 반복 구조
# *****길찾기_반복_1차배열*****
# ====================================

def DFS(g1, g2, v):
    S = []
    visited = [0] * 100
    # 시작점 방문
    visited[v] = 1
    S.append(v)

    while S:
        # v 에서 w 를 방문
        for w in [g1[v], g2[v]]:
            if w != -1 and not visited[w]:  # -1인지 체크해야 한다.
                visited[w] = 1
                S.append(v)
                v = w
                break
        else:
            if not S: break
            v = S.pop()

    return visited[99]


for tc in range(1, 11):
    tc_num, E = map(int, input().split())  # tc 번호, 간선수
    arr = list(map(int, input().split()))

    # g1, g2: 정점마다 최대 2개의 인접정점 저장, 없으면
    # 0번 정점도 사용되고 있으므로, -1로 초기화
    g1 = [-1] * 100  # 정점 번호 0번 ~ 99번
    g2 = [-1] * 100

    # 간선수가 E 이므로 전체 길이는 E*2
    for i in range(0, E * 2, 2):
        u, v = arr[i], arr[i + 1]
        if g1[u] == -1:
            g1[u] = v
        else:
            g2[u] = v

    ans = DFS(g1, g2, 0)

    print(f'#{tc} {ans}')
