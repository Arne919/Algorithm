def is_num(n):  # 숫자가 맞는지 판단 음수나 소수도 숫자인지 판단해야함
    try:
        float(n)
    except:
        return False
    else:
        return True


def cal_formula(trans):  # 후위표현식 연산
    s = []
    for k in trans:
        if is_num(k):  # 숫자면 스택리스트에 삽입
            s.append(float(k))
        elif k == '.':
            if len(s) == 1:  # 스택이 무조건 하나여야만 출력
                return int(s.pop())
            else:
                return 'error'
        else:  # 연산자라면
            if len(s) >= 2:
                n1 = int(s.pop())  # 스택리스트에서 꺼내서 연산후 삽입
                n2 = int(s.pop())  # int 로 형변환
                if k == '+':
                    s.append(n2 + n1)
                elif k == '*':
                    s.append(n2 * n1)
                elif k == '-':
                    s.append(n2 - n1)
                elif k == '/':
                    if n1 == 0:
                        return 'error'
                    else:
                        s.append(n2 / n1)
            else:
                return 'error'  # 연산자가 알 수 없는 연산자 인 경우


T = int(input())
for tc in range(1, T + 1):
    case = input().split()
    result = cal_formula(case)  # 후위표기식연산 함수 호출
    print(f'#{tc} {result}')