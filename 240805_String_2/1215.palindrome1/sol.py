import sys
# '1215.txt' 파일을 입력으로 설정
sys.stdin = open('input.txt')

# 테스트 케이스가 10개 주어지므로 1부터 10까지 반복
for tc in range(1, 11):
    N = 8  # 배열의 크기 (8x8)
    M = int(input())  # 찾으려는 회문의 길이 입력
    arr = [input() for _ in range(N)]  # 8개의 문자열을 입력받아 배열에 저장

    cnt = 0  # 회문 개수를 셀 변수

    # 모든 행에 대해서 반복
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

    # 모든 열에 대해서 반복
    for col in range(N):
        # 현재 열에서 길이 M인 회문을 찾기 위해
        for start in range(0, N-M + 1):
            end = start + M - 1  # 회문의 끝 인덱스
            # 회문 체크 (양쪽 끝에서부터 중간까지 비교)
            for i in range(M//2):
                if arr[start+i][col] != arr[end-i][col]:
                    break
            else:
                # 회문이 발견된 경우
                cnt += 1

    # 테스트 케이스 번호와 함께 회문 개수를 출력
    print(f'#{tc} {cnt}')