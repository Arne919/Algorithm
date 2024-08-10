import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    sellprice = 0
    money = 0
    for i in arr[::-1]:
        if sellprice <= i:
            sellprice = i
        else:
            money += (sellprice - j)

    print(f'#{tc} {money}')