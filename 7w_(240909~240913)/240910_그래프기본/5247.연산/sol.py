import sys
sys.stdin = open('input.txt')

from collections import deque

# bfs탐색
def solve(num):
    global rst
    # print(nums)
    Q = deque()
    # Q에는 현재 숫자와 카운트 해줄 숫자를 튜플로 넣어줌
    Q.append((num, 0))
    # 현재 숫자 방문 체크
    visit.add(num)
    while Q:
        now, cnt = Q.popleft()
        if now == M:
            rst = min(rst, cnt)
            return
        # 갈 수 있는 경로는 4가지
        tmp = [now+1, now-1, now*2, now-10]
        for val in tmp:
            # 방문하지 않았고, 제약조건의 숫자 범위라면 bfs탐색
            if val not in visit and 0 < val <= 1000000:
                visit.add(val)
                Q.append((val, cnt+1))

for tc in range(int(input())):
    N, M = map(int, input().split())

    visit = set()
    rst = 987654321
    solve(N)
    print(f'#{tc+1}', rst)