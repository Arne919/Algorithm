import sys
sys.stdin = open('input.txt')

import copy

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]  # 상하좌우


def fall_block(tmp_data, W, H):
    for y in range(W):
        stack = []
        for x in range(H - 1, -1, -1):
            if tmp_data[x][y] > 0:
                stack.append(tmp_data[x][y])
                tmp_data[x][y] = 0
        for x in range(len(stack)):
            tmp_data[H - 1 - x][y] = stack[x]
    return tmp_data


def boom(x, y, tmp_data, W, H):
    queue = [(x, y, tmp_data[x][y])]    # 조사 대상 q에 삽입
    tmp_data[x][y] = 0                  # 해당 위치 벽돌 부수기.

    while queue:
        x, y, power = queue.pop(0)

        for k in range(4):
            nx, ny = x, y
            for _ in range(power - 1):
                nx += dx[k]
                ny += dy[k]
                if 0 <= nx < H and 0 <= ny < W and tmp_data[nx][ny] > 0:
                    if tmp_data[nx][ny] > 1:
                        queue.append((nx, ny, tmp_data[nx][ny]))
                    tmp_data[nx][ny] = 0

    return fall_block(tmp_data, W, H)


def fall_ball(n, tmp_data):
    global result
    '''
        n : 회차 정보
        tmp_data : 이번 회차 벽돌 상태
    '''
    if n == N:      # 모든 회차 종료시
        # 남아있는 벽돌 수 합산. (벽돌에 적힌 폭탄 수가 아닌, 벽돌 개수를 세어야 함에 주의)
        remaining_bricks = sum(sum(1 for x in row if x > 0) for row in tmp_data)
        result = min(result, remaining_bricks)  # 최솟값 갱신
        return

    # 아직 구슬이 남아 있다면
    for y in range(W):  # 모든 열에 대해서 조사 실행
        x = 0           # 0번쨰 행부터 조사를 하되
        while x < H and tmp_data[x][y] == 0:
            x += 1      # 벽돌이 있는 위치를 찾을 때까지 아래로 전진
        if x == H:      # 탐색 대상이 바닥까지 닿았다면, 해당 위치에서는 깨뜨릴 벽돌이 없으므로 continue
            continue

        new_data = copy.deepcopy(tmp_data)      # 이번 회차만을 위한 복제본 생성
        new_data = boom(x, y, new_data, W, H)   # 벽돌 부수기 시작
        if not any([any(a) for a in new_data]):     # 만약, 모든 벽돌이 부서졌다면,
            result = 0                              # 더 이상 조사 할 필요 없으므로 종료
            return

        fall_ball(n + 1, new_data)      # 제거된 벽돌을 기준으로 다음 회차 진행


T = int(input())
for tc in range(1, T + 1):
    # 구슬 수, 너비, 높이
    N, W, H = map(int, input().split())
    # 벽돌 정보
    data = [list(map(int, input().split())) for _ in range(H)]
    # 충분히 큰 값 : 최대 너비 * 최대 높이
    result = 12 * 15
    fall_ball(0, data)  # 0회차 구슬 떨구기
    print(f'#{tc} {result}')
