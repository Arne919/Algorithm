import sys
sys.stdin = open('input.txt')

for case in range(1, 11):
    count = int(input())
    arr = list(map(int, input().split()))

    for _ in range(count):
        max_v = max(arr)
        min_v = min(arr)

        if max_v - min_v == 0:
            break
        if max_v - min_v == 1:
            break

        arr[arr.index(max_v)] -= 1
        arr[arr.index(min_v)] += 1

    print(f'#{case} {max_v - min_v}')