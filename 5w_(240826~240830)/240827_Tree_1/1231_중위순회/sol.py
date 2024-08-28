import sys
sys.stdin = open('input.txt')

# 중위 순회
def in_order(v):
    if v:
        # 왼쪽 자식
        in_order(left[v])
        result.append(tree[v])
        # print(tree[v], end='')  # visit(v)
        # 오른쪽 자식
        in_order(right[v])

for tc in range(1, 11):
    N = int(input())    #정점 개수
    tree = [0]*(N+1)
    left = [0]*(N+1)            # 왼쪽 자식 번호를 저장할 리스트
    right = [0] * (N + 1)       # 오른쪽 자식 번호를 저장할 리스트
    result =[]
    for _ in range(N):
        node = input().split()
        tree[int(node[0])] = node[1]
        # 왼쪽 자식이 있다면
        if len(node) >= 3:
            left[int(node[0])] = int(node[2])
        # 왼쪽 자식있고 오른쪽 자식도 있음
        if len(node) == 4:
            right[int(node[0])] = int(node[3])
    in_order(1)
    print(f'#{tc} {"".join(result)}')
    # print(f'#{tc} ', end='')
    # in_order(1)
    # print()