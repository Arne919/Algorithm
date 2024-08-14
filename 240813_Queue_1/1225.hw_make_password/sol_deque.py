import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(1, 11):
    _ = input()
    arr = deque(map(int, input().split()))  # 리스트를 deque로 변환

    while arr[-1] > 0:                      # 암호의 마지막 숫자가 0 이하가 될 때까지 반복
        for i in range(1, 6):  # 1부터 5까지의 숫자를 순서대로 빼서 처리
            # front_value = arr.popleft()   # 맨 앞 숫자를 꺼냄
            new_value = arr.popleft() - i   # 차감 연산
            if new_value > 0:               # 차감 후 값이 0보다 크면
                arr.append(new_value)       # 큐의 맨 뒤에 추가
            else:                           # 차감 후 값이 0 이하이면
                arr.append(0)               # 큐의 맨 뒤에 0을 추가
                break                       # 다음 숫자로 넘어감

    result = ' '.join(map(str, arr))        # 결과를 문자열로 변환
    print(f'#{tc} {result}')