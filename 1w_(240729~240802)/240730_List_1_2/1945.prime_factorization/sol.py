import sys
sys.stdin = open('input.txt')

T = int(input())
# 테스트 케이스

for test_case in range(1, T+1): # 테스트케이스 반복
    N = int(input())
    divisor_list = [2, 3, 5, 7, 11] # 약수 리스트
    count_list = [0] * 5        # 나눈 약수 횟수 리스트

    for i in range(5):          # 나눠지는 횟수 계산
        divisor = divisor_list[i]
        while N % divisor == 0: # N이 현재 소수로 나눠질 수 있는 동안 계속 나눔
            N //= divisor
            count_list[i] += 1

    result = ' '.join(map(str, count_list)) # 결과를 문자열로 변환하여 출력 형식에 맞춤
    print(f'#{test_case} {result}')


