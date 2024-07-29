'''
3
5
49679
5
08271
10
7797946543
'''
T = int(input()) #테스트케이스 개수
for test_case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

print(f'#{test_case} BubbleSort')