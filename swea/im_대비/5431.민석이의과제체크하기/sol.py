import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))   # 과제 제출 한 학생
    all = []                                # 학생 전체(아직은 빈 리스트)
    not_arr = []                            # 과제 제출 안 한 학생(여기다 추가 할 예정)

    for i in range(1, N+1):                 # 학생 전체 채우기
        all.append(i)
    
    for student in all:                     # 학생 반복해서
        if student not in arr:              # 제출 안 한 학생 리스트에 추가
            not_arr.append(student)

    result = ' '.join(map(str, not_arr))    # 문자열로 변환
    print(f'#{tc} {result}')