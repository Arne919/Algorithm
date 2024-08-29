# A, B 를 입력받고 더한 값을 출력하세요.
# 2 3

# 코드 제출 or 시험에는 아래코드를 반드시 주석처리!!
import sys
# sys.stdin: 표준입력
# open('input.txt', 'r'): input.txt.를 r(읽기 전용)으로 열겠다.
# 입력텍스트파일에서 shift + F10 누르면 바로 실행
sys.stdin = open('input.txt', 'r')
# sys.stdout: 표준출력
# open('output.txt', 'w'): output.txt를 w(쓰기 전용)으로 열겠다.
sys.stdout = open('output.txt', 'w')


A, B = map(int, input().split())
print(A+B)

