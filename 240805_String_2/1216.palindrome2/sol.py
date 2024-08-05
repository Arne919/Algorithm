import sys
sys.stdin = open('input.txt')

# 테스트 케이스가 10개 주어지므로 1부터 10까지 반복
for tc in range(1, 11):
    N = 8  # 배열의 크기 (8x8)
    M = int(input())  # 찾으려는 회문의 길이 입력
    arr = [input() for _ in range(N)]  # 8개의 문자열을 입력받아 배열에 저장

    cnt = 0  # 회문 개수를 셀 변수

for row in range(N):
    # 현재 행에서 길이 M인 회문을 찾기 위해
    for start in range(0, N-M + 1):
        end = start + M - 1  # 회문의 끝 인덱스
        # 회문 체크 (양쪽 끝에서부터 중간까지 비교)
        for i in range(M//2):
            if arr[row][start+i] != arr[row][end-i]:
                break
        else:
            # 회문이 발견된 경우
            cnt += 1


# def horizontal(arr, leng):
#     for r in arr:
#         for i in range(N-leng+1):
#             for j in range(leng//2):
#                 if r[i+j] != r[i+leng-1-j]:
#                     break
#             else:
#                 return True
#     return False

# for _ in range(10):
#     tc = int(input())
#     N = 100
#     arr1 = list(input() for _ in range(N))
#     arr2 = [''.join(x) for x in zip(*arr1)]
#     for leng in range(N,1,-1):
#         if horizontal(arr1,leng) or horizontal(arr2,leng):
#             break
#     print(f'#{tc} {leng}')

