import sys
sys.stdin = open('input.txt')

N = 100         #사다리 판의 크기 NxN
T = 10
for tc in range(1, T + 1):
    _ = input() # tc 번호(사용하지않는 변수로 주로_ 표기)

    # 길을 찾는 것이기 때문에 굳이 int로 형변환할 이유가 없다.
    arr = [input().split() for _ in range(N)]   #[['1', '0', '0'],['1', ...]]
    # print(arr)  # 실수할 가능성을 줄여주는 소듕한 print 한 줄
    # 시작 지점을 찾는다. 역순으로 탐색 2의 위치를 찾기
    col = 0
    row = N - 1 # 마지막 줄 (2인 idx를 찾음)
    for idx in range(N):
        if arr[row][idx] == '2':    # 문자와 숫자에 대한 데이터 형 구분은 소듕하다.
            col = idx
            break

    # 델타 리스트를 작성
    # 좌측, 우측 탐색을 우선으로 진행하고 마지막에 위로 올라갈 예정
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    # 시작 위치는 row, col
    # 델타 이동을 시작 반복 횟수 => 알수 없음 (N*N 최대반복)
    # 언제까지 반복? -> 시작지점을 찾았을 때까지
    # => row가 0이면 그 때 col이 시작지점
    # => row가 0일때까지 반복이 필요
    while row > 0:
        # 사다리를 역행해서 올라가기
        # 다음 이동할 위치를 찾기(델타로~)
        for k in range(3):  # 좌, 우, 상 순서로 탐색 이동
            # 다음 이동할 칸에 대해 인덱스를 계산
            nr = row + dr[k]    # 현재 위치 + 델타 = 이동위치
            nc = col + dc[k]
            if 0 <= nr < N and 0 <= nc < N: # 사다리 범위 내 일때
                # 사다리가 있는지 확인
                if arr[nr][nc] == '1':      # 이동가능한 위치
                    # 헨젤과 그레텔의 과자 이론을 이용해서 왔던 길 표시
                    arr[row][col] = '0'     # 왔던 길을 '0'으로 표시
                    # 이동 => 현재 위치를 갱신
                    row = nr
                    col = nc
                    break
    # while 이 종료가 됐다! == 입구에 도착했다!
    print(f'#{tc} {col}')

    

