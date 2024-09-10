import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()

    result= 'Possible'
    for i in range(N):  # 손님
        bread = customer[i]//M*K    # c[i]//M 빵만들횟수, *K 한번만들때 빵수
        if bread < i+1:             # 다음손님왔을때 빵이적으면(줄거없음)
            result = 'Impossible'
            break
    print(f'#{tc} {result}')