T = int(input()) #테스트케이스 개수
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count_list = [0]
    for i in range(0, N-1):
        count = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                count += 1
            count_list.append(count)
    max_count = max(count_list)
    print(f'#{test_case} {max_count}')