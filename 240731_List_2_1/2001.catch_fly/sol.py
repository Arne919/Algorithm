import sys
sys.stdin = open('input.txt')

T = int(input())                # 테스트케이스 수
for test_case in range(1, T+1): # 테스트케이스 반복
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] # NxN배열, MxM파리채
    max_kill = 0                                              # 잡을 수 있는 파리의 최댓값
    for i in range(N-M+1):                                    # 배열 넘어가지 않도록 범위
        for j in range(N-M+1):
            kill = 0
            for k in range(M):                                # 파리채 크기만큼 반복
                for l in range(M):
                    kill += arr[i+k][j+l]
            if kill > max_kill:                               # 최대값 갱신
                max_kill = kill
    print(f'#{test_case} {max_kill}')