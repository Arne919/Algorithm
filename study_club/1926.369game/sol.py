import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = [''] * N  # N개의 빈 문자열 리스트

for num in range(1, N + 1):
    num_str = str(num)  # 숫자를 문자열로 변환
    count = 0
    
    for char in num_str:
        if char in '369':
            count += 1  # 3 6 9를 '-'로 대체
    
    if count > 0:
        num_list[num - 1] = '-' * count
    else:
        num_list[num - 1] = num_str

result = ' '.join(num_list) # 리스트를 괄호 없이 출력
print(result)
'''
1 2 - 4 5 - 7 8 - 10 11 12 - 14 15 - 17 18 - 20 21 22 - 24 25 - 27 28 - - - - -- - - -- - - -- 40 41 42 - 44 45 - 47 48 - 50 51 52 - 54 55 - 57 58 - - - - -- - - -- - - -- 70 71 72 - 74 75 - 77 78 - 80 81 82 - 84 85 - 87 88 - - - - -- - - -- - - -- 100
'''


# N = int(input())
# num_list = [''] * N  # N개의 빈 문자열 리스트

# for num in range(1, N + 1):
#     num_str = str(num)  # 숫자를 문자열로 변환
#     new_str = ''
    
#     for char in num_str:
#         if char == '3' or char == '6' or char == '9':
#             new_str += '-'  # 3 6 9를 '-'로 대체
#         else:
#             new_str += char  # 그 외 문자 추가
    
#     num_list[num - 1] = new_str  # 문자열을 추가(순서대로)

# result = ' '.join(num_list) # 리스트를 괄호 없이 출력
# print(result)

'''
1 2 - 4 5 - 7 8 - 10 11 12 1- 14 15 1- 17 18 1- 20 21 22 2- 24 25 2- 27 28 2- -0 -1 -2 -- -4 -5 -- -7 -8 -- 40 41 42 4- 44 45 4- 47 48 4- 50 51 52 5- 54 55 5- 57 58 5- -0 -1 -2 -- -4 -5 -- -7 -8 -- 70 71 72 7- 74 75 7- 77 78 7- 80 81 82 8- 84 85 8- 87 88 8- -0 -1 -2 -- -4 -5 -- -7 -8 -- 100
'''