import sys
sys.stdin = open('input.txt')

def DFS(adjl):
    v2 = 0              # 출발점
    stack = []
    visited = [0] * 100
    visited[v2] = 1     # 방문하면 1로 표시
    stack.append(v2)    # 방금 방문한거 stack에 추가

    while True:
        for w in adjl[v2]:  # v2에서 갈수있는 길(w)
            if visited[w] == 0: # not visited[w] # 방문하지 않은 길
                stack.append(v2)# 스택에 추가
                v2=w            # w에 방문
                visited[w] = 1  # 방문 표시
                break
        else:
            if stack:           # 스택있으면 
                v2 = stack.pop()# stack의 top을 꺼내서 이동
            else:               # 스택없으면 종료
                break
    return visited[99]  # 도착점


for _ in range(1, 11):
    tc, E = map(int, input().split()) # tc, 길의 개수
    

    # 인접 리스트
    adjl = [[] for _ in range(100)]
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjl[v1].append(v2)
        
    print(f'#{tc} {DFS(adjl)}')

