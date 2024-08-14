import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    for i in range(M):
        queue.append(queue.popleft())
        # arr.append(arr[0])
        # arr.pop(0)

    print(f'#{tc} {queue.popleft()}')