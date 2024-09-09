import sys
sys.stdin = open('input.txt')

def search(result, dep):    # result:확률계산하는값, dep:깊이(사람)
    global max_result
    # 유망하지 않을때~~ 고마하자(가지치기)
    # result < max_result 하면 더 많이 못줄여서 타임에러...
    # result = max_result 상황도 이미 단계를 진행할 필요 없다는 거니까 포함
    if result <= max_result: return

    if dep == N:    # 마지막사람까지 일 다하면
        max_result = max(max_result, result)   # 최댓값 갱신
        return
    # else:
    for i in range(N):
        if visited[i] == 0: # 방문을 안했으면
            visited[i] = 1  # 방문함
            # 확률 계산을 위해 원본 값에*0.01해둠    /재귀dfs
            search(result*data[dep][i]*0.01, dep+1)
            visited[i] = 0  # 방문끝~

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # N개의 행:N인원수 열:N개의 일 능률
    data = [list(map(int, input().split())) for _ in range(N)]
    # result = 0
    visited = [0] * N
    max_result = 0  # 비교할 최대 확률(0%가 가장 낮으므로)
    # result: 확률 계산할 초기값은1(~0.00까지 계속 작아질 예정), dep:깊이는 0부터 N까지 1씩 증가할 예정
    search(1, 0)
    print(f'#{tc} {max_result*100:6f}')