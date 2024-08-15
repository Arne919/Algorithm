import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    ball = input()
    result = 0
    result += ball.count('(|')
    result += ball.count('|)')
    result += ball.count('()')

    print(f'#{tc} {result}')