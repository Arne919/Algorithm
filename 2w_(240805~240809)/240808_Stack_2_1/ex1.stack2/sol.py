import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    chars = str(input())
    stack = []
    dict = {'-': 1, '+': 1, '*': 2, '/': 2}
    result = ''
    for char in chars:                  # 문자열에서 한개씩 가져옴
        if char not in dict.keys():     # 문자가 연산자가 아닌것(숫자)
            result += char              # 결과에 추가
        elif char in dict:              # 문자가 연산자라면
            # 스택 있고, top이 문자보다 크거나 같으면
            # ex) 스택에 있는게 * 이고, 현재 연산자가 + 일때 
            if stack and dict[char] <= dict[stack[-1]]:
                result += stack[-1]     # 결과에 top 추가 /*는 결과에 추가하고
                stack.pop()             # 스택에서 꺼냄    /* 스택에서 꺼냄
                # stack.append(char)    # +는 스택에 넣음(아래와 중복되므로 if문 밖에서 추가)
            stack.append(char)          # 그외 조건 연산자들 스택에 추가 /*꺼내고 + 넣어야해서 아래로

    while stack:                        # (남은)스택 다 쓸때까지
        result += stack[-1]             # 결과에 스택 top부터 추가
        stack.pop()                     # 스택에서 꺼냄
    print(f'#{tc} {result}')