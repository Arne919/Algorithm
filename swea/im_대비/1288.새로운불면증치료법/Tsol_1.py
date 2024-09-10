import sys
sys.stdin = open('input.txt')

# 불면증
# set 특징 1. 순서가 없다. 2. 중복을 허용하지 않는다

def count_sheep(N):
    seen = set()
    k = 1

    while len(seen) < 10: # 숫자가 0,1,2,3,4,5,6,7,8,9 ---> 10개
        number = N * k # 예를들어 N이 1295, 5번째 양을 셌을때 모든 숫를 다 보았다.
        seen.update(str(number))
        k += 1 # 예를들어 k = 6이 된다(루프트 5번 실행, k가 6일때 종료)
    return N * (k - 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = count_sheep(N)
    print(f'#{tc} {result}')