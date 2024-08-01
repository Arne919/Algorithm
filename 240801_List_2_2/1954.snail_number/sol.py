import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f"#{tc}")

    dr = [0, 1, 0, -1]  # 우, 하, 좌, 상
    dc = [1, 0, -1, 0]

    N = int(input())    # 배열크기 입력받음 (NxN)

    arr = [[0] * N for _ in range(N)]   # 답을 기록할 배열 초기화 (NxN)

    count = 1           # 점점 증가할 값을 담아두기 위한 변수
    row, col = 0, 0     # 시작 좌표 초기화
    dir = 0             # 이동할 방향(우하좌상)
    arr[row][col] = count   # 시작 위치에 1을 기록하고 시작

    while count < N ** 2:   # NxN배열이라서 N^2 횟수만큼 반복
        nr = row + dr[dir]
        nc = col + dc[dir]
        # 위치가 배열 범위 내에 있고, 변수 기록 안한곳
        if 0 <= nr < N and  0 <= nc < N and arr[nr][nc] == 0:
            count += 1
            arr[nr][nc] = count # 다음 위치에 변수 기록
            row, col = nr, nc   # 위치 이동(갱신)
        else:
            dir += 1            # 방향 전환
            if dir >= 4:        # 다시 우하좌상으로 초기화
                dir = 0

    for i in arr:
        print(' '.join(map(str, i)))  # 문자열로 변환해서 출력
        # print(*i)               # 리스트의 요소들을 언팩해서 출력
    