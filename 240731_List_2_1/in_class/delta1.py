import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1): # 테스트케이스 반복
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    total = 0
    for i in range(N):
        for j in range(N):        # NxN 배열의 모든 원소에 대해
            s = 0                 # 문제에서 원소와 인접원소의 차의 ...합 저장
            for k in range(4):    # i,j 원소의 4방향 원소에 대해
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N: # 실존하는 인접원소 ni,nj
                    s += abs(arr[i][j] - arr[ni][nj])
            total += s
    print(f'#{test_case} {total}')