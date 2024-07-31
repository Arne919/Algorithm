# arr1 = [0] * 3
# arr2 = [[0] * 3 for _ in range(2)]
# print(arr1)             # [0, 0, 0]
# print(*arr1)            # 0 0 0
# for i in range(2):
#     print(*arr2[i])      # [0, 0, 0]
#                         # [0, 0, 0]
#----------------------------------------------
# for i in range(2):
#     for j in range(3):
#         print(arr2[i][j], end = ' ')
#     print()                 # 0 0 0
#                             # 0 0 0
#-------------------------------------
#
# arr= [[1,2,3],[4,5,6]]
# print(len(arr))
# print(len(arr[0])) #xxxxxxxxxxxxxxx
#----------------------------------------------
# i행의 좌표
# j열의 좌표
# 행 우선 순회
# for i in range(n):
#     for j in range(m):
#         f(array[i][j]) # 필요한 연산 수행
# 열 우선 순회
# for j in range(m):
#     for i in range(n):
#         f(array[i][j]) # 필요한 연산 수행
# 지그재그 순회
for i in range(n):
    for j in range(m):
        f(array[i][j+(m-1-2*j)*(i%2)])