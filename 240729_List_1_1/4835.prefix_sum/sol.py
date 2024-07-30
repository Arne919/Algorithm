T = int(input()) #테스트케이스 개수
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_list = []
    for i in range(0, N-M+1):
        allsum = sum(arr[i:i+M])
        sum_list.append(allsum)
    difference = max(sum_list)-min(sum_list)
    print(f'#{test_case} {difference}')