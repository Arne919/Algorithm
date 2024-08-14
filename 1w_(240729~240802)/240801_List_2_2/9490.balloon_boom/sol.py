import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    max_total = 0

    # (a,b)위치 지정
    for a in range(N):
        for b in range(M):
            count = arr[a][b]
            r_total = 0
            c_total = 0
            # 행 기준
            for j in range(b - count, b + count+1):
                if 0 <= j < M:
                    r_total += arr[a][j]
            # 열 기준
            for i in range(a - count, a + count+1):
                if 0 <= i < N:
                    c_total += arr[i][b]
            # 지정한 위치 기준 행 열 더하고 중복된 중앙자리 빼기
            total = r_total + c_total - arr[a][b]
            # 합의 최댓값 갱신
            if max_total < total:
                max_total = total
    print(f"#{test_case} {max_total}")
