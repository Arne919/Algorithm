import sys
sys.stdin = open('input.txt')

T = int(input())                # 테스트케이스 수
for test_case in range(1, T+1): # 테스트케이스 반복
    N = int(input())            # 직사각형의 수 입력
    arr = [[0] * 10 for _ in range(10)] # 10x10 초기화
    find_3 = 0                  # 색상이 3인 셀의 수를 세는 변수 초기화

    for _ in range(N):          # 각 직사각형 입력
        r1, c1, r2, c2, color = map(int, input().split())   # 직사각형의 좌표 및 색상
        for r in range(r1, r2 + 1):                     # 주어진 좌표 범위
            for c in range(c1, c2 + 1):
                if arr[r][c] == 0:                      # 빈 셀인 경우
                    arr[r][c] = color                   # 주어진 색상으로 칠함
                elif arr[r][c] != color:                # 이미 다른 색으로 칠해진 경우
                    arr[r][c] = 3                       # 3 기입
                    find_3 += 1                         # 색상이 3인 셀의 수 count
    print(f'#{test_case} {find_3}')