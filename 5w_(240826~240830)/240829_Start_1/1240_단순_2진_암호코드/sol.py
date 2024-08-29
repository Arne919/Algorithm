import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N, M 입력
    arr = [input() for _ in range(N)]   # NxM 직사각형 배열
    for i in range(N):                  # 암호코드있는 한줄만
        if '1' in arr[i]:
            code = arr[i]
            break

    for j in range(M-1, -1, -1):        # 뒤에서부터 세었을때 1시작할때부터
        if code[j] == '1':
            k = j                       # 찐코드 세어야하는 부분의 마지막 인덱스임
            break

    real_code = []                      # 찐코드를 넣을 리스트
    for l in range(k-55, k+1, 7):       # 7개씩 짤라서 넣음
        real_code.append(code[l:l+7])
    # print(real_code)

    secret_code = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }
    real_real_code = []     # 암호코드 해석한 수의 리스트
    for a in real_code:
        real_real_code.append(secret_code[a])
    # print(real_real_code)

    # 올바른 코드인지 검증단계
    result = 0
    for b in range(4):      # 암호코드 올바른지 판별계산
        result += real_real_code[b*2]*3 + real_real_code[b*2+1]
        
    if result % 10 == 0:   # 암호코드가 10의 배수면 (올바른암호코드 =각자리수합)
        print(f'#{tc} {sum(real_real_code)}')
    else:               # 10배수 아닐때 (잘못된 암호코드 =0)
        print(f'#{tc} {0}')