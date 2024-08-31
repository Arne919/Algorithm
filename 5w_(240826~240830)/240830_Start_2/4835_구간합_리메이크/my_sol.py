import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N=행 수, 이웃한 M개의 합
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 입력받기
    num_row_arr = max(len(row) for row in arr)  # 각 열의 길이중 제일 긴 열의 길이
    col_arr = [[] for _ in range(num_row_arr)]  # 제일 긴 열의 길이에 맞춘 빈 열리스트 생성

    # 행을 순회해서 열리스트로 채우기
    for row in arr: 
        for i in range(num_row_arr):    # 최대 열 갯수만큼 순회
            if i < len(row):            # i 
                col_arr[i].append(row[i])
    # print(col_arr)

    # 이웃한 M개의 요소의 합을 저장할 리스트 초기화
    pairs = []
    # 각 열을 순회해서 연속된 M개 요소의 합 추가
    for col in col_arr:
        if len(col) >=M:
            for i in range(len(col)-M+1):
                pairs.append(sum(col[i:i+M]))
    # print(pairs)    

    # pairs에 리스트 없으면 -1 출력
    if not pairs:
        print(f'#{tc} -1')
    else:   # 최댓값-최솟값 출력
        max_sum = max(pairs)
        min_sum = min(pairs)
        print(f'#{tc} {max_sum - min_sum}')