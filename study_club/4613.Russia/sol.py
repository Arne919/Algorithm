import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # NxM행렬
    arr = [list(input()) for _ in range(N)]
    min_cnt =N*M                        # 최소카운트 N*M

    white_cnt = 0                       # 흰
    for w in range(0, N-2):             # 행 기준
        for i in range(0, M):           # 열
            if arr[w][i] != 'W':        # W 아닌부분 카운트 +1
                white_cnt += 1

        blue_cnt = 0                    # 파랑
        for b in range(w+1, N-1):       # 행 기준
            for i in range(0, M):       # 열
                if arr[b][i] != 'B':    # B 아닌부분 카운트 +1
                    blue_cnt += 1

            red_cnt = 0                 # 빨강
            for r in range(b+1, N):     # 행 기준
                for i in range(0, M):   # 열
                    if arr[r][i] != 'R':# R 아닌부분 카운트 +1
                        red_cnt += 1
    
            cnt = white_cnt + blue_cnt + red_cnt # 카운트 합
            if min_cnt > cnt:           # 최솟값 갱신
                min_cnt = cnt

    print(f'#{tc} {min_cnt}')
