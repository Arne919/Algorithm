import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())  # 소수 입력
    cnt = 0             # 자릿수 세는 변수(초기화)
    result = ''         # 결과(문자열)
    while N != 0:       # N이 0이될때까지 반복
        cnt += 1        # 자릿수+1
        if cnt ==13:    # 13이상되면 overflow처리
            result = 'overflow'
            break
        num = N // 2**-cnt  # 몫만 구함
        result += str(int(num)) # 몫 결과에 추가
        N = N-(num*2**-cnt) # N에 현재 자리의 비트값 뺀걸로 저장
    print(f'#{tc} {result}')