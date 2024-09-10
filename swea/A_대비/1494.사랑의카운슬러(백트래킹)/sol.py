import sys
sys.stdin = open('input.txt')

def combination(start, sum_x, sum_y, cnt):
    global result
    # 결과가 0이면 더이상 진행하지 않고 종료(가지치기1)
    if result == 0:
        return
    # 현재 조합의 점의 수가 N//2에 도달하면
    if cnt == N // 2:
        # 나머지 점들의 합계를 계산
        other_x = total_x - sum_x
        other_y = total_y - sum_y
        # 거리계산+최소값갱신
        result = min(result, (other_x-sum_x)**2+(other_y - sum_y)**2)
        return
    # 재귀 호출
    for i in range(start, N):
        combination(i+1, sum_x+arr[i][0], sum_y+arr[i][1], cnt+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 점 개수
    # 점 좌표 리스트
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 모든 점의 x와 y 좌표의 총합계산
    total_x = sum(x for x, y in arr)
    total_y = sum(y for x, y in arr)

    result = 1e11
    combination(0,0,0,0)
    print(f'#{tc} {result}')
