import sys; sys.stdin = open('input.txt')


def find_palindrome(arr, N, M):
    # 모든 행에 대해서 반복
    for row in range(N):
        # arr[row]행에서 길이 M인 회문을 찾기
        for s in range(0, N - M + 1):
            e = s + M - 1
            # 회문체크
            for i in range(M // 2):
                if arr[row][s + i] != arr[row][e - i]:
                    break
            else:
                ret = ''
                for i in range(M):
                    ret += arr[row][s + i]
                return ret

    # 모든 열에 대해서 반복
    for col in range(N):
        # arr[][col]열에서 길이 M인 회문을 찾기
        for s in range(0, N - M + 1):
            e = s + M - 1
            # 회문체크
            for i in range(M // 2):
                if arr[s + i][col] != arr[e - i][col]:
                    break
            else:
                ret = ''
                for i in range(M):
                    ret += arr[s + i][col]
                return ret
    return None

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = find_palindrome(arr, N, M)

    print(f'#{tc} {ans}')
