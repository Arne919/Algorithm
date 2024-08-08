import sys
sys.stdin = open('input.txt')

def check_match(expression):
    stack = []
    matching_dict = {')': '('}

    for char in expression:
        if char in matching_dict.values():
            stack.append(char)
        elif char in matching_dict.keys():
            if not stack or stack[-1] != matching_dict[char]:
                return -1
            stack.pop()
    if len(stack) == 0:
        return 1
    return -1

T = int(input())
for tc in range(1, T + 1):
    expression = input()
    print(f'#{tc} {check_match(expression)}')
