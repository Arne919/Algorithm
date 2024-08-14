# 달팽이는 패턴이 있음
    # 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for size in range(1, 11):
    
    arr = [[0]*size for _ in range(size)] # 답을 기록할 배열

    count = 1       # 점점 증가할 값을 담아두기 위한 변수
    row, col = 0, 0     # 시작 좌표 초기화
    dir = 0         # 이동할 방향
    arr[row][col] = f'{count:>2}'   # 시작 위치에 1을 기록하고 시작
    while count < size**2: # N*N 만큼의 크기가 만들어지니까 3*3 -> 9
        nr = row + dr[dir]    # nr = 0 + dr[0] -> 0
        nc = col + dc[dir]    # nc = 0 + dc[0] -> 1
        # 다음 이동 위치가 범위 리스트의 범위 내이고,
        # 방문한 적이 없다면
        if 0 <= nr < size and 0 <= nc < size and arr[nr][nc] == 0:
            count += 1      # 값 증가
            arr[nr][nc] = f'{count:>2}' # 새로 가려는 곳에 넣는다
            row, col = nr, nc       # 내 현재 위치를 바꿔준다.
        else:       # 위에서 찾은 모든 조건을 만족하지 못하는 언젠가
            dir += 1
            if dir >= 4:    # 방향은 4종류 뿐
                dir = 0
    # 출력하기
    for i in arr:
        print(*i)
    print()