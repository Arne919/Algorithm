import sys
sys.stdin = open('input.txt')

arr = list(int(input()) for _ in range(9))
# print(arr)
# sum(arr)
# print(sum(arr))
for i in range(len(arr)-1):
    for j in range(i+1,(len(arr))):
        result = sum(arr)-arr[i]-arr[j]
        if result == 100:
            arr.remove(arr[i])
            arr.remove(arr[j])
            list.sort(arr)
            print(arr, end = '')
# print(arr)