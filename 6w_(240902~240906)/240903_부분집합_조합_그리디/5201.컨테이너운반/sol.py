import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split())) # 무게(컨테이너)
    T = list(map(int, input().split())) # 적재용량(트럭)
    W.sort(reverse=True)
    T.sort(reverse=True)
    # print(W)
    # print(T)
    result = [0]*M
    for i in range(N):
        for j in range(M):
            if T[j] >= W[i]:    # 적재가능할때
                if not result[j]:   # 트럭 안쓴거일때
                    result[j] = W[i]    # 결과값에 옮긴 무게 추가
                    break
    print(f'#{tc} {sum(result)}')

