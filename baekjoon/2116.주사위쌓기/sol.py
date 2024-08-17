import sys
sys.stdin = open('input.txt')

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
top_bot = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
# print(dice)
result = []
for i in range(6):                  # 바닥이 1~6일때
    max_dice = []                   # 몸통중 큰 수 리스트(주사위당 1개)
    first = [1,2,3,4,5,6]           # 첫번째 주사위 숫자
    bot = dice[0][i]                # 첫번째주사위 바닥
    top = dice[0][top_bot[i]]       # 첫번째주사위 천장
    first.remove(bot)               # 바닥 제거
    first.remove(top)               # 천장 제거
    max_dice.append(max(first))     # 몸통중에 큰수 추가
    for j in range(1, N):           # 첫번째주사위 제외(그다음)
        next = [1,2,3,4,5,6]        # 다음 주사위 숫자
        bot = top                   # 현주사위바닥=이전주사위천장
        top_index = top_bot[dice[j].index(top)]
        top = dice[j][top_index]    # 현주사위 천장
        next.remove(bot)            # 현주사위 바닥 제거
        next.remove(top)            # 현주사위 천장 제거
        max_dice.append(max(next))  # 몸통중에 큰수 추가
    # print(result)               # 맨바닥이 1~6일때 max총합 list
    result.append(sum(max_dice))
print(max(result))