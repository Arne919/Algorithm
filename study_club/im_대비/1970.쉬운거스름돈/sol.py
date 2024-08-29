import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    money = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_count = []
    # money_count = [0] * 8
    for i in range(8):
        count = 0
        while money >= money_list[i]:
            money -= money_list[i]
            count += 1
        money_count.append(count)
        # money_count[i] = count
    result = ' '.join(map(str, money_count))
    print(f'#{tc}\n{result}')


