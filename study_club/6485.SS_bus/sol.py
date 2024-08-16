import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())    # 정류장의 개수
    C = [int(input()) for _ in range(P)]
    cnt = [0] * P       # 각 정류장의 노선을 셀 리스트

    for i in range(N):  # i번째 버스
        for j in range(line[i][0], line[i][1] + 1):  # i번째 버스 노선
            for k in range(P):  # cnt리스트 반복
                if j == C[k]:   # 버스노선 갯수섹
                    cnt[k] += 1

    result = ' '.join(map(str, cnt))
    print(f'#{tc} {result}')