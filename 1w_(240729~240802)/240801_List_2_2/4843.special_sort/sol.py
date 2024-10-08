import sys
sys.stdin = open('input.txt')

T = int(input())
def bubble(numbers,N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = bubble(numbers,N)
    result = []
    for i in range(5):
        result.append(numbers[N-1-i])
        result.append(numbers[i])
    result = ' '.join(map(str, result))
    print(f'#{tc} {result}')

