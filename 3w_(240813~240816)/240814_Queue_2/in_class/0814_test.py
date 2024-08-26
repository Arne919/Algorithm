import sys
sys.stdin = open('0814_test_input.txt')
sw_count = int(input())
sw_list = list(map(int, input().split()))
student_count = int(input())
student_list = [list(map(int, input().split())) for _ in range(student_count)]

print(sw_list)
# 남학생 1, 여학생 2
for st in student_list:
    gender, number = st

    # 남학생
    if gender == 1:
        for i in range(number - 1, sw_count, number):
            sw_list[i] = 1 - sw_list[i]
        print(sw_list)

    # 여학생
    else:
        # 본인은 무조건 변경
        sw_list[number - 1] = 1 - sw_list[number - 1]

        # 본인을 기준으로 좌우 대칭인 곳까지 스위치를 변경

        loop_cnt = number - 1 if sw_count // 2 >= number else sw_count - number

        for i in range(1, loop_cnt + 1):
            # 좌우가 똑같으면
            if sw_list[number - 1 -i ] == sw_list[number -1 + i]:
                sw_list[number -1 -i] = 1 - sw_list[number - 1 -i]
                sw_list[number -1 +i] = 1 - sw_list[number - 1 +i]
            else:
                break
        print(sw_list)

for i in range(1, sw_count + 1):
    print(sw_list[i - 1], end= " ")
    if i % 20 == 0:
        print()
