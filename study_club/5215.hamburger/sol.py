import sys
sys.stdin = open('input.txt')

def DFS():
    pass



T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())    # 개수, 칼로리제한
    arr = [list(map(int, input().split())) for _ in range(N)]
    best_score = 0


    DFS()
    print(f'#{tc} {best_score}')    
    