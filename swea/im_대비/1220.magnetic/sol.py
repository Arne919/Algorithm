import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1: N극(빨강, 위)      2: S극(파랑, 아래)

    cnt = 0
    for i in range(N):  # 열 고정후 행 반복
        stack = []      # (위는 N극이라 빨강 안없어짐)빨+파 나오면 교착(뺄거임)
        r, c = 0, i

        while r < N:    # 행 끝날때까지
            if len(stack)==0 and arr[r][c]==1:  # 스택 비어있고, 빨강이면 스택에 추가
                # +(스택 비어있는데 파랑이면 없어지는거라 상관x)
                stack.append(1)
            elif len(stack)!=0 and arr[r][c]==2:# 스택안비어있고, 파랑이면 이전꺼(빨강)빼기
                # +(빨간색 스택 누적추가하는 건 어차피 교착에 영향x, 괜히 파랑으로 스택뺄때 교착카운트가 될수있음)
                # +(스택있때 또 빨강 추가하면 교착 카운트 되니까 추가하면 안됌)
                stack.pop()
                cnt += 1                        # 교착 +1
            r += 1      # 행 반복
    print(f'#{tc} {cnt}')