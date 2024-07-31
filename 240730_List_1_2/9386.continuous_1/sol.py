import sys
sys.stdin = open('input.txt')

T = int(input())                            # 테스트케이스 수 T

for test_case in range(1, T + 1):           # 테스트케이스 반복
    N = int(input())                        # 수열의 길이 N
    arr = input()                           # N개의 0과 1로 구성된 수열
    
    max_count = 0                           # 연속한 1의 최대갯수
    count = 0                               # 연속한 1의 개수

    for i in range(N):                      # 수열의 길이만큼 반복
        if arr[i] == '1':                   # 수열의 i위치가 1일때 증가
            count += 1
            if count > max_count:           # 최대갯수 갱신
                max_count = count
        else:                               # 1이 아닐땐 0으로 초기화
            count = 0

    print(f'#{test_case} {max_count}')