import sys
sys.stdin = open('input.txt')

def DFS(adjl, S, G):
    v2 = S              # 출발점
    stack = []          # 스택리스트
    visited = [0] * 50  # 방문체크할 리스트
    visited[v2] = 1     # 방문하면 1로 표시
    stack.append(v2)    # 출발지점 스택에 추가

    while True:
        for w in adjl[v2]:  # 출발점과 이어진 길 반복
            if visited[w] == 0: # 방문안한 w
                v2 = w      # 방문
                stack.append(v2)# 스택에 추가
                visited[w] = 1  # 방문 체크
                break
        else:               # 인접정점 없을 때
            if stack:       # 스택있을때
                v2 = stack.pop()# 이전 방문으로 돌아감
            else:           # 스택없을때
                break       # 종료
    return visited[G]   # 도착점


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # 정점, 간선
    adjl = [[] for _ in range(50)]   # 정점이 50개까지 있음
    arr = [list(map(int, input().split())) for _ in range(E)] # 간선개수만큼 리스트로 짜기
    S, G = map(int, input().split()) # (출력할)출발,도착노드 입력

    for i in range(E):               # 쌍으로 v1, v2로 등록 후 추가
        v1, v2 = arr[i][0], arr[i][1]
        adjl[v1].append(v2)

    print(f'#{tc} {DFS(adjl, S, G)}')