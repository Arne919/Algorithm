import sys
sys.stdin = open('input.txt', encoding='utf-8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    search_text = input()
    result = 0

    pattern_idx = 0
    compare_idx = 0

    while compare_idx < len(search_text):
        if search_text[compare_idx] != pattern[pattern_idx]:
            compare_idx = compare_idx - pattern_idx + 1
            pattern_idx = 0
            continue

        pattern_idx += 1
        compare_idx += 1

        if pattern_idx == len(pattern):
            result += 1
            pattern_idx = 0
            compare_idx = compare_idx - pattern_idx + 1
    print(f'#{tc} {result}')