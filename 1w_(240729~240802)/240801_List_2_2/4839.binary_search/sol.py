import sys
sys.stdin = open('input.txt')

T = int(input())

def binary_search(start, end, key, cnt):
    if start > end:
        return False
    mid = (start + end) // 2
    cnt += 1
    if key == mid:
        return cnt
    elif key < mid:
        return binary_search(start, mid, key, cnt)
    elif key > mid:
        return binary_search(mid, end, key, cnt)

for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    A_cnt = binary_search(1, P, A, 0)
    B_cnt = binary_search(1, P, B, 0)
    if A_cnt == B_cnt:
        print(f"#{test_case} 0")
    elif A_cnt < B_cnt:
        print(f"#{test_case} A")
    elif A_cnt > B_cnt:
        print(f"#{test_case} B")

