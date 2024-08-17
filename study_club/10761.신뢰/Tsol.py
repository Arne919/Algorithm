T = int(input())
for tc in range(1, T + 1):
    arr = input().split()
    time = 0 # 총 소요시간 초기화
    robot = {'B' : [1, 0], 'O' : [1, 0]} #로봇 : [위치, 마지막 동작 시간] 초기화

    for i in range(1, len(arr), 2):
        type, btn_pos = arr[i], int(arr[i + 1]) # 로봇의 타입, 버튼의 위치
        dist = abs(btn_pos - robot[type][0]) # 거리 ---> abs(버튼의 위치 - 로봇의 위치)
        diff_time = time - robot[type][1] # 시간차이 ---> (현재 시간 - 로봇의 마지막 동작 시간)

        # dist > diff_time 일때:
        # 로봇이 아직 버튼 위치에 도달하지 못했다
        # ex) 로봇 위치 : 1, 버튼 위치 : 5 , dist == 4
        # 마지막 동작 후 3초가 지났다 diff_time 3이다
        # 이 경우는 dist > diff_time ---> 추가로 필요한 시간
        # (4 - 3) + 1 == 2초
        # 반면에 로봇이 위치 : 1, 버튼 위치 : 3, dist == 2
        # 마지막 동작 후 3초가 지났다 diff_time 3이다
        # 이 경우는 dist <= diff_time ---> 로봇이 이미 버튼에 도달했거나 지나쳤음
        # 필요한 시간 1초 추가

        if dist <= diff_time:# 로봇이 이미 버튼에 도착했거나 지나쳤다면
            time += 1 # 버튼 누르는 시간 추가
        else: # 로봇이 아직 버튼에 도착하지 않았다면
            time += dist - diff_time + 1 # 이동시간과 버튼 누르는 시간 +

        robot[type] = [btn_pos, time] # 로봇의 새 위치, 새 동작시간 갱신

    print(f'#{tc} {time}')