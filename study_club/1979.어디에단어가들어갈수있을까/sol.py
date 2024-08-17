import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())        # NxN, K = 단어길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0     # 단어길이 세기
        # 가로
        for j in range(N):
            if arr[i][j] == 1:              # 현위치가 1이면
                cnt += 1                    # 단어길이 세기
            if arr[i][j] == 0 or j == N-1:  # 0이거나, 벽만나면
                if cnt == K:                # 단어길이 = K일때
                    result += 1             # 결과값 +1
                cnt = 0                     # 초기화
                
		#세로
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == N-1:
                if cnt == K:
                    result+=1
                cnt = 0
            
    print(f'#{tc} {result}')