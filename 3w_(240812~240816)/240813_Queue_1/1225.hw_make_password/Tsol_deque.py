import sys
from collections import deque

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    password = deque(list(map(int, input().split())))
    cnt = 1  # 싸이클이 진행되며 증가하며 단계별 요소값에서 빼야할 값

    # 마지막 요소가 0 or 0 보다 작을 때까지 반복
    while password[-1] > 0:
        # 맨 앞의 데이터 추출
        pop_data = password.popleft()

        # 현재 cnt 만큼 수를 빼줌
        pop_data -= cnt
        # cnt를 감소한 값이 0 보다 작은 경우 0으로 고정
        if pop_data < 0:
            pop_data = 0

        # 맨 앞에서 꺼낸 후 계산한 값을 맨 뒤에 삽입
        password.append(pop_data)

        cnt += 1  # 감소 간격 1 증가
        if cnt > 5:  # 한 번의 싸이클(5)를 다 돈 경우, 다시 1로 초기화
            cnt = 1

    print(f'#{tc}', end=' ')
    print(*password)
