import sys
sys.stdin = open('input.txt')

N = 100
T = 10
for tc in range(1, T + 1):
    _ = input()
    
    arr = [input().split() for _ in range(N)]   # 2차 배열 입력
    col = 0
    row = N - 1                                 # 마지막 줄(에서 2찾기)
    for idx in range(N):
        if arr[row][idx] == '2':                # 문자와 숫자 데이터 형 구분!(중요)
            col = idx
            break
    
    dr = [0, 0, -1] # 좌, 우, 상
    dc = [-1, 1, 0]
    while row > 0:  # 첫 행이 되면 끝
        for k in range(3):
            nr = row + dr[k]
            nc = col + dc[k]
            if 0 <= nr < N and 0 <= nc < N: # 사다리 범위 내
                if arr[nr][nc] == '1':      # 1인 이동 가능위치 확인
                    arr[row][col] = '0'     # 중복안되도록 있던곳 0으로 변경
                    row = nr                # 1있던곳으로 이동(갱신)
                    col = nc
                    break
    print(f'#{tc} {col}')