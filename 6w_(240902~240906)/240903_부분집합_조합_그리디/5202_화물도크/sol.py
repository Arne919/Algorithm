import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])    # 종료 시간을 기준으로 오름차순
    # print(arr)
    cnt = 0
    now = 0
    for i in range(N):
        s = arr[i][0]   # 시작 시간
        e = arr[i][1]   # 종료 시간
        if now <= s:
            cnt += 1
            now = e
    print(f'#{tc} {cnt}')