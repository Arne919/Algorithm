from collections import deque

T = int(input())
for tc in range(1, T + 1):
    arr = input().split()
    robot, blue, orange = deque(), deque(), deque()

    for idx in range(1, len(arr), 2):
        r_turn, pos = arr[idx], arr[idx + 1]
        robot.append(r_turn)
        if r_turn == 'B':
            blue.append(int(pos))
        else:
            orange.append(int(pos))
    time = 0
    b_pos, o_pos = 1, 1
    while robot:
        time += 1
        c_pos = robot[0]

        if blue:
            if b_pos < blue[0]:
                b_pos += 1
            elif b_pos > blue[0]:
                b_pos -= 1
            else:
                if c_pos == 'B':
                    robot.popleft()
                    blue.popleft()
        if orange:
            if o_pos < orange[0]:
                o_pos += 1
            elif o_pos > orange[0]:
                o_pos -= 1
            else:
                if c_pos == 'O':
                    robot.popleft()
                    orange.popleft()


    print(f'#{tc} {time}')