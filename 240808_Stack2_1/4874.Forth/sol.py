# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#     chars = list(input().split())
#     stack = []
#     # try:
#     for char in chars:                  # 문자열에서 한개씩 가져옴
#         if char.isnumeric:              # 문자가 숫자면
#             stack.append(int(char))     # 스택에 넣음
#         elif char == '.':
#             if len(stack) == 1:
#                 result = stack[-1]
#                 stack.pop()
#             else:
#                 result = 'error'
#                 break
#         else:
#             if len(stack) < 2:
#                 result = 'error'
#                 break
#             else:
#                 if char == '+':
#                     result = stack[-2] + stack[-1]
#                     stack.pop()
#                     stack.pop()
#                     stack.append(result)
#                 elif char == '-':
#                     result = stack[-2] - stack[-1]
#                     stack.pop()
#                     stack.pop()
#                     stack.append(result)
#                 elif char == '*':
#                     result = stack[-2] * stack[-1]
#                     stack.pop()
#                     stack.pop()
#                     stack.append(result)
#                 elif char == '/':
#                     result = stack[-2] // stack[-1]
#                     stack.pop()
#                     stack.pop()
#                     stack.append(result)
#
#     #     while stack:                        # (남은)스택 다 쓸때까지
#     #         result += stack[-1]             # 결과에 스택 top부터 추가
#     #         stack.pop()                     # 스택에서 꺼냄
#     #     # print(f'#{tc} {result}')
#     # except:
#     #     result = 'error'
#
#     print(f'#{tc} {result}')