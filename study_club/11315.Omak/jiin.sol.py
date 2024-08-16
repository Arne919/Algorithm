T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().strip())) for _ in range(N)]

    omok = ['o'] * 5
    result = 'NO'

    # 열 탐색
    if result == 'NO':
        for i in range(N):
            for j in range(N):
                col = [arr[i][j] for i in range(N)]
                if col == omok:
                    result = 'YES'
                    break

    # 오른 대각
    if result == 'NO':
        result_list = []
        for i in range(N - 5 + 1):
            for j in range(N - 5 + 1):
                for k in range(5):
                    if arr[i+k][j+k] == 'o':
                        result_list.append('o')
                        if result_list == omok:
                            result = 'YES'
                    else:
                        result_list = []

    # 왼 대각
    if result == 'NO':
        result_list2 = []
        for a in range(4, N):
            for b in range(N - 5 + 1):
                for k in range(5):
                    if arr[a-k][b+k] == 'o':
                        result_list2.append('o')
                        if result_list2 == omok:
                            result = 'YES'
                    else:
                        result_list2 = []

    print(f'#{tc} {result}')