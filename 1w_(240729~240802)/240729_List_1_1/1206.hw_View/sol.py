T = 10 #테스트케이스 개수
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    view = 0
    # new_list = []
    for i in range(2, N-2):
        if arr[i] > arr[i+1] and arr[i] > arr[i+2] and arr[i] > arr[i-1] and arr[i] > arr[i-2]:
            new_list = [arr[i+1], arr[i+2], arr[i-1], arr[i-2]]
            max_new_list = max(new_list)
            view += arr[i] - max_new_list
    print(f'#{test_case} {view}')