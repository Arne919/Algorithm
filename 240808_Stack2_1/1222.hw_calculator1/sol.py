import sys
sys.stdin = open('input.txt')

# for tc in range(1, 11):
#     N = int(input())
#     chars = list(input().split())
#     stack = []
#     dict = {'-': 1, '+': 1, '*': 2, '/': 2}
#     result =''
#     for char in chars:
#         if char not in dict.keys():
#             result += char
#         elif char in dict:
#             if stack and dict[char] <= dict[stack[-1]]:
#                 result += stack[-1]
#                 stack.pop()
#                 stack.append(char)
#     while stack:
#         result += stack[-1]
#         stack.pop()
#     print(f'#{tc} {result}')