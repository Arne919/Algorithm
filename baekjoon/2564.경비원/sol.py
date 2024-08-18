import sys
sys.stdin = open('input.txt')

# 방향마다의 위치 계산 (북쪽왼쪽부터 0)
def cal(location,distance):
    if location == 1:   # 북
        return distance
    elif location == 4: # 동
        return x+distance
    elif location == 2: # 남
        return x+y+x-distance
    elif location == 3: # 서
        return x+y+x+y-distance


x, y = map(int, input().split())    # x:가로, y:세로
store = int(input())                # 상점 갯수
# 상점위치, 동근위치 입력받기
locations = [list(map(int, input().split())) for _ in range(store+1)]
arr=[]
for i in range(store+1):
    location, distance = locations[i][0], locations[i][1]
    arr.append(cal(location, distance))
# 동근이 위치 계산
DG_loc = arr[-1]

result = 0
for i in range(store):
    cal_dist = abs(arr[i]-DG_loc)
    total = 2*(x+y)
    result += min(cal_dist, total-cal_dist)
print(result)
