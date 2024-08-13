import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    
    numbers = set()
    nx, count = n, 1
    while True :
        temp = set(str(nx))
        numbers.update(temp)
        
        if len(numbers) == 10 :
            break
        count += 1
        nx = n * count
    print(f'#{tc} {nx}')