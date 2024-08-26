import sys
from collections import deque

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    password = deque(list(map(int, input().split())))
    cnt = 1  # 싸이클이 진행하는동안 단계별 값에서 빼는 count

    # 마지막 요소가 0보다 크면 계속해서 아래 로직을 진행
    while password[-1] > 0:
        # 맨 앞의 데이터를 추출
        pop_data = password.popleft()

        # cnt만큼 빼준다.
        pop_data -= cnt
        # 뺀 값이 음수면, 0으로 만든다.
        if pop_data < 0:
            pop_data = 0
        # 맨 앞에서 꺼낸 값을 뺀 다음에 맨 뒤에다가 다시 집어넣는다.
        password.append(pop_data)
        cnt += 1
        if cnt > 5:
            cnt = 1

    print(f'#{tc}', end=' ')
    print(*password)
