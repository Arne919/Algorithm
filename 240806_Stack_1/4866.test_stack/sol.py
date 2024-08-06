import sys
sys.stdin = open('input.txt')

def match(chars):
    stack = []
    dict = {')': '(', '}': '{'}

    for char in chars:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if not stack or stack[-1] != dict[char]:
                return 0
            stack.pop()
    if len(stack) == 0:
        return 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    chars = input()
    print(f'#{tc} {match(chars)}')