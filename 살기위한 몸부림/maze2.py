import sys
sys.stdin = open('maze2_input.txt')

def DFS(start):
    global N, arr

    row, col = start[0], start[1]  # 시작 지점의 행과 열을 설정
    dr = [0, 1, 0, -1]  # 방향 배열: 우, 하, 좌, 상 (시계 방향)
    dc = [1, 0, -1, 0]
    stack = [(row, col)]  # 스택에 시작 지점을 추가
    arr[row][col] = 1  # 시작 지점을 방문 표시

    while stack:  # 스택이 비어있지 않은 동안 반복
        row, col = stack.pop()  # 스택에서 현재 위치를 꺼냄
        for k in range(4):  # 네 방향에 대해 탐색
            nr = row + dr[k]  # 새로운 행 위치
            nc = col + dc[k]  # 새로운 열 위치

            # 범위 내에 있고, 방문하지 않은(0) 경우
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                stack.append((nr, nc))  # 스택에 새로운 위치 추가
                arr[nr][nc] = 1  # 방문 표시
            # 도착 지점(3)을 찾은 경우
            elif arr[nr][nc] == 3:
                return 1  # 탐색 성공, 1 반환

    return 0  # 탐색 실패, 0 반환

for tc in range(1, 11):  # 총 10개의 테스트 케이스를 반복
    T = int(input())  # 테스트 케이스 번호 입력 (사용되지 않음)
    N = 100  # 미로의 크기
    arr = [list(map(int, input())) for _ in range(N)]  # 100x100 미로 입력
    start = []  # 시작 지점 초기화
    
    for r in range(N):  # 시작 지점 찾기
        for c in range(N):
            if arr[r][c] == 2:  # 시작 지점(2) 발견 시
                start.append(r)
                start.append(c)
    
    print(f'#{tc} {DFS(start)}')  # DFS 함수 호출 후 결과 출력