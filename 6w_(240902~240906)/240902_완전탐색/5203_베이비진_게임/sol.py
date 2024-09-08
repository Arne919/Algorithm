import sys
sys.stdin = open('input.txt')

def babygin(lst, i):
    if lst[i] >= 3:
        return True
    if lst[i - 2] and lst[i - 1] and lst[i]:
        return True
    if i < 8 and lst[i] and lst[i + 1] and lst[i + 2]:
        return True
    if i < 9 and lst[i - 1] and lst[i] and lst[i + 1]:
        return True
    return False

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    card_1 = [0] * 10
    card_2 = [0] * 10

    i = 0
    result = 0
    for i in range(0, 12):
        if i % 2 == 0:
            card_1[cards[i]] += 1
            if babygin(card_1, cards[i]):
                result = 1
                break
        else:
            card_2[cards[i]] += 1
            if babygin(card_2, cards[i]):
                result = 2
                break
    print(f'#{tc} {result}')