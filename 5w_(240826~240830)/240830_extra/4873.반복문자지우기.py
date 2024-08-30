import sys
sys.stdin = open('4873.input.txt')

def repeat_str(chars):
    stack = []
    for char in chars:
        if len(stack) == 0 or char != stack[-1]:
            stack.append(char)
        elif char == stack[-1]:
            stack.pop()
    return len(stack)

T = int(input())
for tc in range(1, T+1):
    chars = input()
    print(f'#{tc} {repeat_str((chars))}')