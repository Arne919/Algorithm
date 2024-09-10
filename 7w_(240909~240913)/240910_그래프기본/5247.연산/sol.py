import sys
sys.stdin = open('input.txt')

from collections import deque

# bfs탐색
def bfs(num):
    global result
    # print(nums)
    Q = deque()
    # Q에는 현재 숫자와 카운트 해줄 숫자를 튜플로 넣어줌
    Q.append((num, 0))
    # 현재 숫자 방문 체크
    visited.add(num)
    while Q:
        now, cnt = Q.popleft()
        if now == M:
            result = min(result, cnt)
            return
        # 갈 수 있는 경로는 4가지
        tmp = [now+1, now-1, now*2, now-10]
        for val in tmp:
            # 방문하지 않았고, 제약조건의 숫자 범위라면 bfs탐색
            if val not in visited and 0 < val <= 1000000:
                visited.add(val)
                Q.append((val, cnt+1))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = set()
    result = 10*10
    bfs(N)
    print(f'#{tc}', result)