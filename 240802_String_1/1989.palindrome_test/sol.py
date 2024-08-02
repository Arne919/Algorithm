import sys
sys.stdin = open('input.txt')

T = int(input())                # 테스트 케이스 T 입력
for tc in range(1, T + 1):
    word = str(input())
    new_word = word[::-1]
    result = 0
    if word == new_word:
        result = 1
    print(f'#{tc} {result}')

# for tc in range(1, T + 1):
#     word = list(map(str, input()))
#     N = len(word)
#     result = 0
#     new_word = []
#     for i in range(N):
#         new_word.append(word[N-1-i])
#     if new_word == word:
#         result = 1
#     print(f'#{tc} {result}')