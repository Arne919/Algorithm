T = int(input())
for tc in range(1, T + 1):
    s = input()
    stack = [] # 빈 스택
    cnt = 0

    for i in range(len(s)):
        # 열린 괄호를 만난 경우
        if s[i] == '(':
            stack.append('(')
        # 잡초를 만난 경우
        elif s[i] == '|':
            if stack and stack[-1] == '(': # 스택이 비어있지 않고, 마지막 요소가 열린 괄호일 경우
                stack.pop() # 스택에서 '('를 제거
                cnt += 1
            else:
                stack.append('|')
        # 닫힌 괄호 만난 경우
        elif s[i] == ')':
            if stack and stack[-1] == '|':
                stack.pop()
                cnt += 1
            elif stack and stack[-1] == '(':
                stack.pop()
                cnt += 1

    print(f'#{tc} {cnt}')