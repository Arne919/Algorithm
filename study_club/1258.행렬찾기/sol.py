import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    matrix = []                 # 찾은 행렬 저장 ex)[[1곱,1세,1가],[2곱,2세,2가]] <<곱낮은순, 행작은순
    cnt = 0                     # 행렬 개수
    for r in range(N):          # 시작위치
        for c in range(N):
            r_cnt = 0                   # 세로 초기화
            for i in range(r, N):
                if arr[i][c] == 0:      # 0 발견시 세로탐색 종료
                    break
                else:
                    r_cnt += 1          # 세로 +1칸
                    c_cnt = 0           # 가로 초기화
                for j in range(c, N):
                    if arr[i][j] == 0:  # 0 발견시 가로탐색 종료
                        break
                    else:
                        c_cnt += 1      # 가로 +1칸
                        arr[i][j] = 0   # 확인한 위치는 0으로 변경(방문확인)
            if r_cnt * c_cnt != 0:      # 찾은 행렬(곱,세,가) matrix에 추가
                matrix.append([r_cnt*c_cnt, r_cnt, c_cnt])
                cnt += 1                # 찾은 행렬의 개수 +1

    # print(f'#{tc} {cnt} {matrix}')    # 행렬 확인용
    print(f'#{tc} {cnt}', end=' ')

    # 행렬 크기 정렬
    for j in range(cnt):
        for i in range(cnt-1-j):
            if matrix[i][0] > matrix[i+1][0]:
                matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
            elif matrix[i][0] == matrix[i+1][0]:
                if matrix[i][1] > matrix[i+1][1]:
                    matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
    for j in range(cnt):
        print(matrix[j][1], matrix[j][2], end=' ')
    print()

    # for row in matrix:                        # 람다정렬로 풀면 3줄이지만
    #     print(row[1], row[2], end=' ')        # 못쓰면 버블정렬로 10줄가량 만들면됨^,^
    # matrix.sort(key=lambda x: (x[0], x[1]))


