# 불면증
# set 특징 1, 순서가 없다. 2. 중복을 허용하지 않는다

def count_sheep(N):
    seen = set()
    k = 1

    while len(seen) < 10:   # 숫자가 0~9 ->10개
        number = N * k      # 예를 들어 N이 1295, 5번째 양을 셌을때 모든 숫자를 다봄
        seen.update(str(number))
        k += 1              # k가 6이 된다 (루프트5번실행, k가 6일때 종료)
    return N * (k - 1)
