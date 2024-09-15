# dfs bfs문제
# 인접행렬 방식과 인접리스트 방식 두개다 모두 익숙해지기

N,M,V = map(int, input().split())
node = {}
for i in range(N):
    node[i+1] = []

for i in range(M):
    x, y = map(int, input().split())
    node[x].append(y)
    node[y].append(x)

for i in range(1, N+1): # 정렬을 해주고 돌려줘야 값이 재대로 나온다 인접리스트라 그런가?
    node[i].sort()      # {1: [2, 3], 2: [5, 1], 3: [4, 1], 4: [5, 3], 5: [4, 2]} => {1: [2, 3], 2: [1, 5], 3: [1, 4], 4: [3, 5], 5: [2, 4]}



visited = []

# 스택으로 dfs를 구현할 경우 순서가 거꾸로 나옴...
# def dfs(node,V): # dfs 인접리스트로 풀면 역순?? 그렇게 나와서 안되는것 같다 인접행렬로 풀어보자
#     stack = [V]
#     visited = []
#     while stack:
#         current_node = stack.pop()
#         visited.append(current_node)
#         for i in node[current_node]:
#             if i not in visited and i not in stack:
#                 stack.append(i)
        
#     return visited

def dfs(node, start, visited):
    visited.append(start)
    for i in node[start]:
        if i not in visited:
            dfs(node, i, visited)
    return 


# def bfs(node,V):
#     queue = [V]
#     visited = []
#     while queue:
#         current_node = queue.pop(0)
#         visited.append(current_node)
#         for i in node[current_node]:
#             if i not in visited and i not in queue:
#                 queue.append(i)
#     return visited

def bfs(node,V): 
    queue = [V]
    visited = [V] # 시작노드를 추가해주고 시작한다.
    while queue:
        current_node = queue.pop(0)
        for i in node[current_node]:
            if i not in visited: # 이 코드가 조건문도 한개더 안넣어도 되고 위에 bfs보다 빠르다.
                queue.append(i)
                visited.append(i) # visited 노드에 추가해준다
    return visited

dfs(node, V, visited)
b_node = bfs(node, V)

for i in visited:
    print(i, end=" ")
print()
for i in b_node:
    print(i, end=" ")