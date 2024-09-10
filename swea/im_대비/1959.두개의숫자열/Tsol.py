import sys
sys.stdin = open('input.txt')

# keymap : vscode keymap 적용
def kim_moo_yeol(A, B):
    # 항상 B가 A보다 더 긴 리스트여야 한다
    if len(A) > len(B):
        A, B = B, A

    max_sum = float('-inf')
    # B 리스트 에서 A 리스트 슬라이딩하며 모든 가능한 위치 순회
    # 예를들어 M = 5, N = 3 ---> [0, 1, 2], [1, 2, 3], [2, 3, 4] ---> M - N + 1
    for i in range(len(B) - len(A) + 1):
        cur_sum = 0 # 현재 위치에서의 곱의 합
        for j in range(len(A)):
            cur_sum += A[j] * B[i + j]

        max_sum = max(max_sum, cur_sum)

    return max_sum

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = kim_moo_yeol(A, B)
    print(f'#{tc} {result}')