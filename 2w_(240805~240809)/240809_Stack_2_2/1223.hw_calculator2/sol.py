import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    chars = input()
    stack = []
    result = ''
    dict = {'+': 1, '*': 2}

    for char in chars:
        if char in dict:         # 문자가 연산자일때
            # 스택이 있고, 우선순위가 높은 연산자가 스택안에 있을때
            while stack and dict[char] <= dict[stack[-1]]:
                result += stack[-1] # top을 결과에 추가하고
                stack.pop()         # 스택에서 꺼냄
            stack.append(char)      # 현 연산자 스택에 추가
        else:                       # 숫자일때 추가
            result += char
    while stack:                    # (남은)스택 다 쓸때까지
        result += stack[-1]         # 결과에 스택 top부터 추가
        stack.pop()                 # 스택에서 꺼냄
    
    for i in result:                # 후위 표기법으로 변환된 식 계산하기
        if i in dict:               # 문자가 연산자일때
            b = stack.pop()         # stack top 두개 뽑아서
            a = stack.pop()
            if i == '+':            # + 일때 더하고 
                stack.append(a + b)
            elif i == '*':          # * 일때 곱하기
                stack.append(a * b)
        else:                       # 숫자일때 스택에 추가
            stack.append(int(i))
    print(f'#{tc} {stack[-1]}')

# result += stack[-1]
# stack.pop()
# result += stack.pop()