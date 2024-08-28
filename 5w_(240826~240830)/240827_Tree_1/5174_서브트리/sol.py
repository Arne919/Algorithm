import sys
sys.stdin = open('input.txt')

def search(node):
    global cnt
    if node:
        cnt+=1
        search(tree[node][0])
        search(tree[node][1])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 2
    tree = [[0, 0] for _ in range(V)]

    for i in range(E):
        parent = arr[i*2]
        child = arr[i*2+1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
    cnt = 0
    search(N)
    print(f'#{tc} {cnt}')