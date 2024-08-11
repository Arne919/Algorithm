import sys
sys.stdin = open('input.txt')

T = int(input())            # tc
for tc in range(1, T+1):
    N = int(input())        # 입력받는 N(숫자)
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]    # 모든숫자들 리스트
    k = 1                   # 배수

    while len(num) != 0:    # num리스트가 빈배열이 되면 종료
        result = N * k           # 입력받은 N의 k배수
        for i in str(result):    # m의 자리수 분해
            i = int(i)      # int로 다시 형변환
            if i in num:    # 자리수가 num리스트에 있으면
                num.remove(i)   # num에서 제거
        k += 1              # 배수 +1
    print(f'#{tc} {result}')     # 출력은 마지막 m값