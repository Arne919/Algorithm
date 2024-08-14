import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    chars = input()
    stack = []
    result = ''

    for char in chars:
        if char == '+':         # 문자가 +일때
            while stack:        # 스택 비울때까지 결과에 추가 후 스택에서 제거
                result += stack[-1]
                stack.pop()
            stack.append(char)  # 현 연산자 스택에 추가
        else:                   # 숫자일때 추가
            result += char
    while stack:                # 스택 비울때까지 결과에 추가 후 스택에서 제거
        result += stack[-1]
        stack.pop()
    
    for i in result:            # 후위 표기법으로 변환된 식 계산하기
        if i == '+':            # 문자가 +일때
            stack.append(stack.pop()+stack.pop())   # 스택에서 숫자 두개꺼내서 더하고 결과를 다시 스택에 추가
        else:                   # 숫자일때 스택에 추가
            stack.append(int(i))
    print(f'#{tc} {stack[-1]}')

# stack.pop()
# stack.append(char)
# => stack[-1] = char