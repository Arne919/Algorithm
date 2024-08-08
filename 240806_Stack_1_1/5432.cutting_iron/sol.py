import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    iron = input()
    stack = []
    cnt = 0

    for i in range(len(iron)):
        if iron[i] == "(":          # 여는 괄호일때
            stack.append("(")       # 스택에 추가
        else:                       # 닫는 괄호일때
            if iron[i-1] =="(":     # 이전문자가 여는괄호일때(레이저)
                stack.pop()         # 이전문자 제거
                cnt += len(stack)   # 현재 스택의 개수 더함
            else:                   # 이전문자가 닫는괄호일때(막대기하나끝)
                stack.pop()         # 이전문자 제거
                cnt += 1            # 막대기 하나 끝으로 +1
    print(f'#{tc} {cnt}')