import sys
sys.stdin = open('input.txt')


for _ in range(10):
    tc = int(input())
    pattern = input()
    search_text = input()
    result = 0              #패턴 일치 횟수

    # 비교할 부분을 가리키는 패턴의 인덱스
    # 비교할 부분을 가리키는 문자열의 인덱스
    pattern_idx = 0
    compare_idx = 0

    # 버블정렬처럼 찾으려고 하는 문자열의 처음부터 시작해서 문자열의 끝까지 진행
    while compare_idx < len(search_text):
        if search_text[compare_idx] != pattern[pattern_idx]:
            compare_idx = compare_idx - pattern_idx + 1
            pattern_idx = 0
            continue
        # 패턴이 같은 경우에는
        # 패턴의 위치도 한 칸 앞으로
        # 현재 비교해야하는 문자도 한 칸 앞으로
        pattern_idx += 1
        compare_idx += 1

        # 모든 문자열을 비교한 경우
        if pattern_idx == len(pattern):
            result += 1     # 패턴 찾은 것 기록
            pattern_idx = 0 # 패턴은 처음 위치부터 다시 비교 시작
            compare_idx = compare_idx - pattern_idx + 1
    print(f'#{tc} {result}')



    print(f'#{tc}')