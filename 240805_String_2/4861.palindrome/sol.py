import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # arr = [list(map(str, input().split())) for _ in range(N)]

    result = []
    # 배열 입력 받기
    arr= []
    for i in range(N):
        arr.append(input())

    # 가로 검색
    for r in range(N):  # r은 row c는 column
        for c in range(N - M + 1):
            if arr[r][c: c + M] == arr[r][c: c + M][::-1]:  # 회문이 맞는지 확인
                result.append(''.join(arr[r][c: c + M]))  # 회문이면 결과 리스트에 추가

    # 세로 검색
    for r in range(N - M + 1):
        for c in range(N):
            c_list = []  # 새로 열 리스트를 만들어주기
            for j in range(M):
                c_list.append(arr[r + j][c])
            if c_list == c_list[::-1]:  # 세로줄이 회문이면
                result.append(''.join(c_list))  # 결과리스트에 추가.

    result = ''.join(result)
    print(f'#{tc} {result}')



    # arr = []
    #
    # for i in range(N):
    #     string = str(input())
    #     arr.append(string)
    #     for j in range(N-M+1):
    #         end = M+j
    #         if string[j:end] == string[j:end][::-1]:
    #             result = string[j:end]
    #
    # vert_arr = []
    #
    # for j in range(N):
    #     vertstr = str()
    #     vert = []
    #     for i in range(N):
    #         vert.append(arr[i][j])
    #     vertstr = ''.join(vert)
    #     vert_arr.append(vertstr)
    #     for k in range(N-M+2):
    #         end = M+k
    #         if vertstr[k:end] == vertstr[k:end][::-1]:
    #             result = vertstr[k:end]

    # print(f'#{tc} {result}')