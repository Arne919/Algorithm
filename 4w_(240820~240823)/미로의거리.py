import sys
sys.stdin = open('miro_way.txt')

def dfs(x, y):
    visited = [[0] * N for _ in range(N)]  # 방문 여부를 체크할 2차원 리스트 초기화
    stack = [(x, y)]  # 스택에 시작 좌표 추가
    dr = [0, 1, 0, -1]  # 행 이동 방향 (우, 하, 좌, 상)
    dc = [1, 0, -1, 0]  # 열 이동 방향 (우, 하, 좌, 상)

    while stack:
        x, y = stack.pop(0)  # 스택에서 좌표를 꺼냄
        if maze[x][y] == 0 or maze[x][y] == 2:  # 현재 좌표가 길이거나 출발점일 때
            maze[x][y] = 1  # 방문 처리

            for k in range(4):  # 네 방향으로 이동
                nr = x + dr[k]  # 다음 행 좌표 계산
                nc = y + dc[k]  # 다음 열 좌표 계산

                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:  # 범위 안에 있고 방문하지 않았을 때
                    if maze[nr][nc] == 3:  # 도착점에 도달했을 때
                        return visited[x][y]  # 현재까지의 이동 횟수 반환
                    elif maze[nr][nc] == 0:  # 길일 때
                        stack.append((nr, nc))  # 스택에 추가
                        visited[nr][nc] = visited[x][y] + 1  # 이동 횟수 증가
    return 0  # 도착점에 도달하지 못했을 때

T = int(input())  # 테스트 케이스 수 입력
for tc in range(1, T + 1):
    N = int(input())  # 미로의 크기 입력
    maze = [list(map(int, input())) for _ in range(N)]  # 미로 정보 입력

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:  # 출발점 찾기
                row, col = r, c  # 출발점 좌표 저장

    print(f'#{tc} {dfs(row, col)}')  # DFS 수행 후 결과 출력
