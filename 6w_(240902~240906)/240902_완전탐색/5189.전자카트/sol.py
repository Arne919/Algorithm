import sys
sys.stdin = open('input.txt')

def battery(num, start, total):
    global result
    # 구하려는 최솟값보다 큰값이면 더 실행 x
    if result < total:
        return
    if num == N-1:   # 마지막에 사무실을 갈때 사용량을 더한다
        total += arr[start][0]
        if result > total:  # 최소합 갱신
            result = total
            return

    for i in range(1, N):
        if visited[i] == 0  and start != i: # 방문안한곳, (n,n)아닌곳일때
            visited[i] = 1  # 방문체크
            battery(num+1, i, total+arr[start][i])  # 더하고 다음열로 넘어가
            visited[i] = 0  # 방문해제


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] *N
    result = 100*N
    battery(0, 0, 0)
    print(f'#{tc} {result}')