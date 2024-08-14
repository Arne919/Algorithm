import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
result = []
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N : 피자를 동시에 구울수있는 화덕 / M : 구워야하는 피자 개수
    cheese = list(map(int, input().split()))    # 피자위에 치즈 list
    inpizza = [(i+1, cheese[i]) for i in range(M)]
    queue = deque([])
    for _ in range(N):
        queue.append(inpizza.pop(0))
    while queue:
        if len(queue) == 1:             # 피자 1개 남을때까지 반복
            v = queue.popleft()
            result.append(v[0])
            break
        num, remain = queue.popleft()
        if remain // 2 != 0:
            queue.append((num, remain //2))
        else:
            if len(inpizza) >= 1:
                queue.append(inpizza.pop(0))
for i, value in enumerate(result):
    print(f'#{tc} {value}')



# T = int(input())
# for tc in range(1, T + 1):
#     #N개의 피자를 동시에 구울 수 있는 화덕
#     #M개의 피자를 구워야 함
#     N, M = map(int, input().split())
#     temp = input().split()
#     #인덱스랑 합쳐서 만들기
#     pizza = [(i+1, int(temp[i])) for i in range(M)]
#     #화덕에 들어갈 피자
#     pizzas = pizza[:N]
#     #화덕에 못들어간 피자
#     pizza = pizza[N:]
#     #피자가 1개남을때까지 반복
#     while len(pizzas) != 1:
#         #피자를 꺼내서 치즈를 반절로 줄이고
#         num, cheese = pizzas.pop(0)
#         cheese //=2
#         #치즈가 있다면 다시 넣는다.
#         if cheese: pizzas.append((num, cheese))
#         #치즈가 없다면 대기중인 피자를 넣어준다,
#         else :
#             if pizza : pizzas.append(pizza.pop(0))
#     print(f'#{tc} {pizzas.pop()[0]}')