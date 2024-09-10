import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str = input()
    cnt = 0
    for i in range(len(str)-1):
        if str[i] == '(':
            if str[i+1] == '|':
                cnt += 1
            elif str[i+1] == ')':
                cnt += 1
        elif str[i] == '|':
            if str[i+1] == ')':
                cnt += 1
    print(f'#{tc} {cnt}')