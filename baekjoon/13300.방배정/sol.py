import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())
room = [[0,0] for _ in range(6)] # [여,남] * 6
result = 0

for i in range(N):
    S, Y = map(int,input().split())
    if S == 0:
        room[Y-1][0] += 1
    else:
        room[Y-1][1] += 1
print(room)
# for grade in students:
#     for num in grade:
#         res+=num//K
#         if num % K: # 만약 남은 인원이 있다면(나머지)
#             res+=1 # 방이 하나더 필요
    
# print(res)