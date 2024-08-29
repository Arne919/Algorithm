import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N, hex_num = map(str, input().split())  # 자리수(N), N자리 16진수
#     dec_num = int(hex_num, 16)              # 10진수로 바꿈
#     bin_num = bin(dec_num)[2:].zfill(4)     # 2진수로 바꿈 앞에 0있어도 4자리 나오도록
#     print(f'#{tc} {0}{bin_num}')

T = int(input())
for tc in range(1, T+1):
    N, hex_num = map(str, input().split())  # 자리수(N), N자리 16진수
    hex_arr = []
    dec_arr = []
    bin_arr = []
    for i in range(len(hex_num)):
        hex_arr.append(hex_num[i])
    # print(hex_arr)
        dec_arr.append(int(hex_arr[i], 16))
        bin_arr.append(bin(dec_arr[i])[2:].zfill(4))
    # print(bin_arr)
    print(f'#{tc} {"".join(bin_arr)}')