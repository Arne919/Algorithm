import sys
sys.stdin = open('input.txt')

T = int(input())                # 테스트케이스 수

for test_case in range(1, T+1): # 테스트케이스 반복
    N, M = map(int, input().split())                            # 행(N) 열(M)
    arr = [list(map(int, input().split())) for _ in range(N)]   # NxM 배열 입력

    # 현재위치+4방향위치
    di = [0, 0, 1, 0, -1]
    dj = [0, 1, 0, -1, 0]

    max_sum = 0                         # 최대 합계를 저장할 변수 초기화
    for i in range(N):
        for j in range(M):              # NxN 배열
            s = 0                       # 현재 원소와 인접원소의 합을 저장할 변수 초기화
            for k in range(5):          # 5방향 반복
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<M: # 실존하는 인접원소 ni,nj(범위내에 있는지)
                    s += arr[ni][nj]    # 유효한 이웃 원소의 값 합산
            if s > max_sum:             # 최대값 갱신
                max_sum = s
    print(f'#{test_case} {max_sum}')