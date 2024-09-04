import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N,  M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for num in B:
        left, right, flag = 0, N - 1, -1 # left, right< 이분탐색을 위한 초기값/flag<초기상태
        while left <= right:            # 이분탐색 진행
            mid = (left + right) // 2   # 중간 인덱스 계산
            # 중간 값이 찾는 값과 같으면 카운트를 증가시키고 탐색 종료
            if A[mid] == num:
                cnt += 1
                break
            # 중간 값이 찾는 값보다 크면 오른쪽 절반을 탐색 범위를 줄임
            if A[mid] > num:
                right = mid - 1
                if flag == 0: break # 이전에 왼쪽 절반을 탐색한 경우, 더이상 탐색x
                flag = 0    # 현재 왼쪽 절반 탐색 중
            # 중간 값이 찾는 값보다 작으면 왼쪽 절반을 탐색 범위를 줄임
            elif A[mid] < num:
                left = mid + 1
                if flag == 1: break  # 이전에 오른족 절반을 탐색한 경우, 더이상 탐색x
                flag = 1    # 현재 오른쪽 절반 탐색 중
    print(f'#{tc} {cnt}')