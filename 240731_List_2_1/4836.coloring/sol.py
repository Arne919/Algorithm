import sys
sys.stdin = open('input.txt')
'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''

T = int(input())                # 테스트케이스 수
arr = list(map(int, input().split()))
# arr = [r1, c1, r2, c2, color]

for (r1, c1, r2, c2, color) in regions:
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if (r, c) not in color_map:
                color_map[(r, c)] = color
            elif color_map[(r, c)] != color:
                color_map[(r, c)] = 3

for test_case in range(1, T+1): # 테스트케이스 반복
    N = int(input())


    # max_sum = 0                         # 최대 합계를 저장할 변수 초기화
    for i in range(10):
        for j in range(10):              # NxN 배열
            [arr[0],[arr[1]]
            if s > max_sum:             # 최대값 갱신
                max_sum = s



    print(f'#{test_case} {result}')