import sys

sys.stdin = open('input.txt')
N = 100
T = 10
for tc in range(1, T + 1):
    _ = input()  # Test case number, not used directly

    arr = [input().split() for _ in range(N)]  # Reading the grid

    # Find the starting column with '1' in the last row
    col = 0
    row = N - 1  # Start from the last row
    for idx in range(N):
        if arr[row][idx] == '1':
            col = idx
            break

    # Initialize the minimum count of moves
    min_count = float('inf')

    # Direction vectors: left, right, up
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    # Try all possible starting positions in the last row
    for start_col in range(N):
        if arr[N-1][start_col] == '1':
            count = 0
            current_col = start_col
            current_row = N - 1
            while current_row > 0:  # Traverse from bottom to top
                for k in range(3):
                    nr = current_row + dr[k]
                    nc = current_col + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == '1':
                            arr[current_row][current_col] = '0'  # Mark the path
                            current_row = nr
                            current_col = nc
                            count += 1
                            break
                else:
                    break  # If no valid move, break out of the loop

            min_count = min(min_count, count)  # Track the minimum moves

    print(f'#{tc} {min_count}')

# N = 100
# T = 10
# for tc in range(1, T + 1):
#     _ = input()
#
#     arr = [input().split() for _ in range(N)]  # 2차 배열 입력
#     col = 0
#     row = N - 1  # 마지막 줄(1에서 start)
#     for idx in range(N):
#         if arr[row][idx] == '1':  # 문자와 숫자 데이터 형 구분!(중요)
#             col = idx
#             break
    # count = 0
    # min_count = 100*100

    #
    # for line in arr[row][idx]:
    #     while row > 0:  # 첫 행이 되면 끝
    #         for k in range(3):
    #             nr = row + dr[k]
    #             nc = col + dc[k]
    #             if 0 <= nr < N and 0 <= nc < N:  # 사다리 범위 내
    #                 if arr[nr][nc] == '1':  # 1인 이동 가능위치 확인
    #                     arr[row][col] = '0'  # 중복안되도록 있던곳 0으로 변경
    #                     count += 1
    #                     row = nr  # 1있던곳으로 이동(갱신)
    #                     col = nc
    #                     break
    #     if min_count >= count:
    #         min_count = count
    # print(f'#{tc} {min_count}')