import sys
sys.stdin = open('4408_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * 200
    for room in rooms:
        if room[0] < room[1]:
            start = (room[0]+1)//2
            end = (room[1]+1)//2
        else:
            end = (room[0]+1)//2
            start = (room[1]+1)//2
        for i in range(start, end+1):
            cnt[i]+=1           # 지나간 복도에 카운트 +1 씩
    result = max(cnt)           # 중복된 복도의 최댓값

    print(f'#{tc} {result}')