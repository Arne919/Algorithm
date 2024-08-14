import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    count = 0
    max_count = 0
    for i in str1:
        for j in str2:
            if i == j:
                count += 1
        if max_count < count:
            max_count = count
        count = 0
    print(f'#{tc} {max_count}')