import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    str_arr = list(map(str, input()))
    for i in range(len(str_arr)):
        if str_arr[i] == 'd':
            str_arr[i] = 'b'
        elif str_arr[i] == 'b':
            str_arr[i] = 'd'
        elif str_arr[i] == 'p':
            str_arr[i] = 'q'
        elif str_arr[i] == 'q':
            str_arr[i] = 'p'
    str_arr = str_arr[::-1]
    print(f"#{tc} {''.join(str_arr)}") 