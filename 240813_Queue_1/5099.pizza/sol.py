import sys
sys.stdin = open('input.txt')

from collections import deque


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N : 피자를 동시에 구울수있는 화덕 / M : 구워야하는 피자 개수
    pizza = list(map(int, input().split()))
    inpizza = [(i, pizza[i]) for i in range(min(N, M))]
    pizza = pizza[N:]       # 화덕에 아직 안들어간 피자

    while len(inpizza) > 1:             # 피자 1개 남을때까지 반복
        num, cheese = inpizza.pop(0)    # 화덕에서 첫번째 피자꺼냄
        cheese //= 2                    # 화덕피자의 치즈는 //2
        if cheese > 0:                  # 치즈가 있으면 다시 넣음
            inpizza.append((num, cheese))
        elif pizza:                     # 치즈 없으면 꺼내고 다른피자 넣기
            inpizza.append((len(inpizza) + len(pizza), pizza.pop(0)))
    print(f'#{tc} {inpizza[0][0]}')