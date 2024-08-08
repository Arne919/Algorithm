import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    chars = input().split()
    stack = []
    result = ''

    for char in chars:                  # 문자열에서 한개씩 가져옴
        if char.isdigit():              # 문자가 숫자면
            stack.append(int(char))     # 스택에 넣음
        elif char == '.':               # 문자인데 .일때
            if len(stack) == 1:         # 스택에 1개 들어가있을때
                result = stack[-1]      # 결과로 출력
                stack.pop()             # 스택에서 꺼냄
            else:                       # 1개가 아닐때 오류 처리
                result = 'error'
                break
        else:
            if len(stack) < 2:          # 연산자가 2개 미만일때 오류처리
                result = 'error'
                break
            else:
                b = stack.pop()         # 스택에서 두 숫자를 꺼내서 연산
                a = stack.pop()
                try:
                    if char == '+':     # 문자가 + 일때 더해서 결과로 넣고
                        stack.append(a + b)
                        # result = stack[-2] + stack[-1]
                    elif char == '-':
                        stack.append(a - b)
                    elif char == '*':
                        stack.append(a * b)
                    elif char == '/':
                        stack.append(a // b)
                    
                except:
                    result = 'error'
                    break

    print(f'#{tc} {result}')
