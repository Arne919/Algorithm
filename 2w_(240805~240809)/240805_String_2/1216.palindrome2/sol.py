import sys
sys.stdin = open('input.txt')


def horizontal(arr, M):
    for row in arr:
        for start in range(N - M + 1):              # 회문 시작지점
            end = start + M - 1                     # 회문 마지막지점 인덱스
            for i in range(M//2):                   # 회문 체크(양 끝)
                if row[start + i] != row[end - i]:  # 회문 아닌경우
                    break
            else:
                return M                            # 회문의 길이 반환

for _ in range(1, 11):
    tc = int(input())
    N = 100                                         # 100x100 배열
    arr1 = [input() for _ in range(N)]              # arr1 배열입력
    arr2 = list(map(list, zip(*arr1)))              # arr1를 행렬바꿈
    for M in range(N, 1, -1):                       # 길이 긴 순으로 max찾으면 이후로는 계산 안해도 됨
        if horizontal(arr1, M) or horizontal(arr2, M):  
            break                                   # 회문 발견시 종료

    print(f'#{tc} {M}')