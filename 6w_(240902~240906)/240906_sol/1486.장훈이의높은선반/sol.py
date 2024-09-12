import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))

    sums_list = [0]
    for i in range(N):
        for j in range(len(sums_list)):
            val = data[i] + sums_list[j]
            sums_list.append(val)
    result = []
    for x in sums_list:
        if x - B >= 0:
            result.append(x-B)
    min_result = min(result)
    print(f'#{tc} {min_result}')