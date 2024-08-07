import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0

    for row in range(N):
        crop = 0
        if row <= N//2:
            for col in range((N-1)//2-row, (N-1)//2+row+1):
                crop += arr[row][col]
        else: # N//2 < row
            row1 = N-1-row
            for col in range((N-1)//2-row1, (N-1)//2+row1+1):

                crop += arr[row][col]
        result += crop
    print(f'#{tc} {result}')

# print(1//2)       # 0
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# result = 0
# crop = 0
# for row in range(3):
#     for col in range(2, 3):
#         print(arr[row][col])

