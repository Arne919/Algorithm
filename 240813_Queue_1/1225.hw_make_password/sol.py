import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    _ = input()
    arr = list(map(int, input().split()))

    while arr[-1] > 0:              # 암호를 찾는 과정에서 0이하의 숫자가 나올때까지
        for i in range(1, 6):       # 1~5의 숫자를 돌아가며 빼준다
            if arr[0] - i > 0:        # 맨앞숫자를 계산했을때 0보다 크면 맨뒤로 보낸다
                arr.append(arr[0] - i)
                arr.pop(0)
            else:                   # 맨앞숫자를 계산했을때 0보다 작으면 앞에서 제거하고 맨뒤에 0을 추가
                arr.append(0)
                arr.pop(0)
                break
    result = ' '.join(map(str, arr))    # 형변환
    print(f'#{tc} {result}')