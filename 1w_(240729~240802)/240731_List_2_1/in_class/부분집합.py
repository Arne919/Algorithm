arr = [3,6,7,1,5,4]
n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (i<<j):
            print(arr[j], end=',')
    print()
print()

# arr = [3,6,7,1,5,4]
# arr = [0,0,0,0]
# for i in range(2):
#     arr[0] = i
#     for j in range(2):
#         arr[1] = j
#         for k in range(2):
#             arr[2] = k
#             for l in range(2):
#                 arr[3] = l
#                 print(arr)