import sys
sys.stdin = open('input.txt')

def making_tree(node):
    global cnt
    if node < V:
        making_tree(node*2)
        cnt += 1
        tree[node] = cnt
        making_tree(node*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = N+1
    tree = [0]*V
    cnt = 0
    making_tree(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')