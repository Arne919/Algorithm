import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(str, input())) for _ in range(5)]
    new_arr = ''

    for c in range(15):
        for r in range(5):
            try:
                new_arr += arr[r][c]
            except:
                new_arr += ''
            # if c < len(arr[r]):
            #     new_arr += arr[r][c]

    print(f'#{tc} {new_arr}') 