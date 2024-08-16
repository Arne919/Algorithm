import sys
sys.stdin = open('input.txt')

arr = list(int(input()) for _ in range(9))
# print(arr)
total = sum(arr)
# print(sum(arr))
for i in range(len(arr)-1):
    for j in range(i+1,(len(arr))):
        # result = total-arr[i]-arr[j]
        if sum(arr)-arr[i]-arr[j] == 100:
            arr.remove(arr[i])
            arr.remove(arr[j])
            list.sort(arr)
            print(*arr)