import sys
sys.stdin = open('4835.input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_list = []
    for i in range(N-M+1):
        all_sum = sum(arr[i:i+M])
        sum_list.append(all_sum)
    difference = max(sum_list)-min(sum_list)
    print(f'#{tc} {difference}')