import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = [''] * N  # N개의 빈 문자열 리스트

for num in range(N):
    num_str = str(num)  # 숫자를 문자열로 변환
    new_str = ''
    
    for char in num_str:
        if char == '3' or char == '6' or char == '9':
            new_str += '-'  # 3 6 9를 '-'로 대체
        else:
            new_str += char  # 그 외 문자 추가
    
    num_list[num] = new_str  # 문자열을 추가(순서대로)

result = ' '.join(num_list) # 리스트를 괄호 없이 출력
print(result)