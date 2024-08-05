import sys
sys.stdin = open('input.txt')

T = int(input())
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # 비교할 정렬된 리스트
dr = [0, 1, 1, 1, 0, -1, -1, -1]             # i 방향으로 더할 값
dc = [1, 1, 0, -1, -1, -1, 0, 1]             # j 방향으로 더할 값

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 0
    r = 0

    for i in range(9):
        a, b = [], []
        for j in range(9):
            a.append(arr[i][j])
            b.append(arr[j][i])
            if (i-1) % 3 == 0 and (j-1) % 3 == 0:
                s = [arr[i][j]]
                for k in range(8):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    s.append(arr[nr][nc])
                if sorted_arr == sorted(s):
                    result += 1
        if sorted(a) == sorted(b) == sorted_arr:
            result += 1
    if result == 18:
        r = 1
    print(f'#{tc} {r}')