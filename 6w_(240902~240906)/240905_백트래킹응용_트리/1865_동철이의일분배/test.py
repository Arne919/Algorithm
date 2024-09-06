import sys
sys.stdin = open('input.txt')


def workpower(result, person):  # result: 확률 계산해가는 값 , person:깊이,i번째사람
    global max_result
    # global visited
    # 끝까지 계산하지 않고 하는 도중에 가망이 없을 때...
    # (**1미만을 곱하면 점점 작아지니깐) 끝까지 더 가지 말고 돌아간다.
    # N<=16이므로 최악 16!까지 가는 것을 사전에 방지하는 작업!!!
    # 주의!!!:: (중간 혹은 최종)result < (최종)max_result 하면 볼 것을 많이 줄이지 못해 타임에러
    # (중간)result == (최종)max_result 은 상황은 이미 단계를 진행할 필요가 없는 것임.
    if result <= max_result:
        return
    # 기본파트, 깊이 제일 밑 끝
    if person == N:  # 모든 직원이 각 자 일을 맡아 다 할때, 최종결과랑 비교
        if max_result <= result:
            max_result = result
        return
    # 재귀파트
    for j in range(N):  # 전체를 도는데
        if visited[j] == 0:  # 방문을 안했으면
            visited[j] = 1  # 방문한다
            workpower(result * arr[person][j] * 0.01, person + 1)  # 재귀 DFS
            visited[j] = 0  # 방문다했다


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N개의 행:N인원수 열:N개의 일 능률
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_result = 0  # 비교할 최대 확률(0%가 가장 낮으므로)
    # result: 확률 계산할 초기값은 1(~0.00까지 계속 작아질 예정) , person:깊이는 0부터 N까지 1씩 증가할 예정
    workpower(1, 0)
    print(f'#{tc} {max_result * 100:6f}')
