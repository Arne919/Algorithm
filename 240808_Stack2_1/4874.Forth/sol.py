import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    chars = list(input().split())
    stack = []
    # try:
    for char in chars:                  # 문자열에서 한개씩 가져옴
        if char.isdigit():            # 문자가 숫자면
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
                if char == '+':         # 문자가 + 일때 더해서 결과로 넣고
                    result = stack[-2] + stack[-1]
                    stack.pop()         # 스택에서 숫자 두개 꺼내고
                    stack.pop()
                    stack.append(result)# 계산한 값 스택에 추가
                elif char == '-':
                    result = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif char == '*':
                    result = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif char == '/':
                    result = stack[-2] / stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(result)
    print(f'#{tc} {result}')

    #     while stack:                        # (남은)스택 다 쓸때까지
    #         result += stack[-1]             # 결과에 스택 top부터 추가
    #         stack.pop()                     # 스택에서 꺼냄
    #     # print(f'#{tc} {result}')
    # except:
    #     result = 'error'