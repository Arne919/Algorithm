import sys
sys.stdin = open('input.txt')

T = int(input())                        # tc
for tc in range(1, T+1):
    N, Q = map(int, input().split())    # 입력받는 N(숫자), Q(범위갯수)
    boxes = [0] * N                     # 빈 박스
    for i in range(1, Q + 1):           # 범위
        L, R = map(int, input().split())# i범위의 시작과 끝 입력받음
        for j in range(L-1, R):         # 범위의 j번째 (인덱스와 위치를 헷갈리지말자)
            boxes[j] = i                # i범위의 상자들의 숫자를 i로 변경
    result = ' '.join(map(str, boxes))
    print(f'#{tc} {result}')
