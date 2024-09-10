import sys
sys.stdin = open('input.txt')

# 시간 초과뜸
def bfs(s, e):
    q = []
    v = [0]*1000001     # 1 ~ 1000000 범위

    q.append(s)
    v[s]=1

    while q:
        c = q.pop(0)
        if c==e:        # 정답을 찾았음
            return v[c]-1

        # 네방향, 범위내, 중복X
        for n in ((c+1), (c-1), (c*2), (c-10)):
            if 1<=n<=1000000 and v[n]==0:
                q.append(n)
                v[n]=v[c]+1
    return -1           # 만들수 없는 숫자 (이경우는 불가능하지만..)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    result = bfs(N, M)
    print(f'#{tc} {result}')