# N = 5
# arr = [55, 7, 78, 12, 42]
import sys
sys.stdin = open('input.txt')



def bubble_sort(arr):                  # 정렬할 리스트, N 원소 수
    # 1. n-1번째 부터 조사
    for i in range(len(arr)-1, 0, -1): # 각 구간의 끝 인덱스 i
        for j in range(i):             # 이전 요소가 이후 요소보다 크면 교환
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# print(*arr)
    return arr
numbers = list(map(int, input().split()))
print(bubble_sort(numbers))