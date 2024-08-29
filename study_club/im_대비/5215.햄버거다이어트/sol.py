import sys
sys.stdin = open('input.txt')

def DFS(i, taste, kcal):
    global best_taste
    if kcal > L:
        return
    if kcal <= L:
        if best_taste < taste:
            best_taste = taste
    for j in range(i,N):
        DFS(j+1, taste + food[j][0], kcal+food[j][1])


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())    # 개수, 칼로리제한
    food = [list(map(int, input().split())) for _ in range(N)]
    best_taste = 0
    DFS(0,0,0)
    print(f'#{tc} {best_taste}')
    