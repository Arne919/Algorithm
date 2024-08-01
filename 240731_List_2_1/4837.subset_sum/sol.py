import sys
sys.stdin = open('input.txt')

T = int(input())
arr = list(range(1, 13))                  # 1~12의 숫자를 원소로 갖는 집합 A

for test_case in range(1, T + 1):
    N, K = map(int, input().split())    # N개의 원소/원소의 합:K
    cnt = 0                           # 원소의 합이 K인 부분집합 개수 초기화
    for i in range(1 << 12):            # 부분집합개수만큼 2 ** n 반복
        subset = []
        for j in range(12):             # 원소의 수만큼 비트를 비교
            if i & (1 << j):
                subset.append(arr[j])     # j번 원소를 subset에 넣기
        if len(subset) == N and sum(subset) == K:
            cnt += 1                  # N과 K에 맞는 부분집합 개수 세기
    print(f'#{test_case} {cnt}')