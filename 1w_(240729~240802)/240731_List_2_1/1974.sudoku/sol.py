import sys
sys.stdin = open('input.txt')

T = int(input())                # 테스트케이스 수
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # 비교할 정렬된 리스트
di = [0, 1, 1, 1, 0, -1, -1, -1]             # i 방향으로 더할 값
dj = [1, 1, 0, -1, -1, -1, 0, 1]             # j 방향으로 더할 값
n = 9                               # 배열 행, 열 길이

for test_case in range(1, T+1):     # 테스트케이스 반복
    arr = [list(map(int, input().split())) for _ in range(n)] # 배열 입력받기
    result = 0                      # 스도쿠 검증 결과 횟수
    r = 0                           # 최종 출력결과

    for i in range(n):              # 행 순회
        a, b = [], []                 # 행, 열 요소 확인용 리스트
        for j in range(n):          # 열 순회
            a.append(arr[i][j])
            b.append(arr[j][i])
            if (i-1) % 3 == 0 and (j-1) % 3 == 0:
                s = [arr[i][j]]
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    s.append(arr[ni][nj])
                if sorted_arr == sorted(s):
                    result += 1
        if sorted(a) == sorted(b) == sorted_arr:
            result += 1
    if result == 18:
        r = 1
    print(f'#{test_case} {r}')