import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    p, q, r, s, w = map(int, input().split())

    if w <= r:
        cost1 = q
    else:
        cost1 = q+s*(w-r)
    cost2 = p*w
    
    if cost1 < cost2:
        min_cost = cost1
    else:
        min_cost = cost2
        
    print(f'#{tc} {min_cost}')