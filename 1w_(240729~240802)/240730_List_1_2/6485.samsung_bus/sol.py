import sys
sys.stdin = open('input.txt')

T = int(input())                # 테스트케이스 수

for test_case in range(1, T+1): # 테스트케이스 반복
    N = int(input())            # 구간의 개수

    A = [0] * N                 # 구간의 시작과 끝을 저장할 리스트
    B = [0] * N

    for i in range(N):          # 각 구간의 시작과 끝을 입력받음
        A[i], B[i] = map(int, input().split())

    P = int(input())            # 확인할 숫자의 개수 P

    C = [0] * P                 # 확인할 숫자를 저장할 리스트
    for i in range(P):
        C[i] = int(input())

    count = [0] * P             # 각 숫자가 구간 내에 포함되는 횟수를 저장할 리스트

    for i in range(N):          # 각 구간을 반복하여 구간에 포함된 숫자를 확인
        for j in range(A[i], B[i]+1):   # 구간의 시작과 끝을 반복
            for k in range(P):          # 확인할 숫자 리스트 반복
                if j == C[k]:           # 숫자가 구간에 포함되면 카운트 +1
                    count[k] += 1

    result = ' '.join(map(str, count))
    print(f'#{test_case} {result}')

