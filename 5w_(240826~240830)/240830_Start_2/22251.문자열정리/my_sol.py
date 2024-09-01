import sys
sys.stdin = open('input.txt')


# 연속적으로 차례로 나열되는 알파벳 확인 함수
def alph(char1, char2):
    # 알파벳 순서 리스트
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    # 소문자로 변경 후, 알파벳리스트에서 인덱스 찾기
    idx1 = alphabet.index(char1.lower())
    idx2 = alphabet.index(char2.lower())
    # 연속되는 문자인지 확인
    return idx2 == idx1 + 1


# 점수 계산 함수
def cal_score(data):
    total_score = 0   # 총 점수를 저장할 변수

    while True:
        new_str = []  # 새문자열을 저장할 리스트
        i = 0
        score = 0
        while i < len(data):
            cnt = 1   # 연속된 문자의 개수
            # 현재,다음 문자가 동일한 경우 cnt+1
            while i + 1 < len(data) and data[i] == data[i + 1]:
                cnt += 1
                i += 1
            if cnt > 1:
                score += cnt  # 연속된 문자 개수만큼 점수 추가
            else:
                new_str.append(data[i])  # 연속하지 않은 문자 -> new_str에 추가
            i += 1
        if score == 0:  # 더 이상 연속된 문자가 없으면 종료
            break
        total_score += score    # 총점수에 점수 추가
        data = ''.join(new_str) # 남은 문자열 합쳐서 data로 초기화

    i = 0   # 동일한문자 뺀 data를 다시 점검
    while i < len(data) - 1:    # 문자열의 각 문자 살핌 <<이거 넣으니까 AXYZA 안된던거 해결
        cnt = 1  # 연속된 알파벳의 개수 (다시 1로 초기화 위에랑 겹칠수도 있어서)
        # 알파벳 순서대로 나열된 문자 점수 계산 (alph 함수)
        while alph(data[i], data[i + 1]):
            cnt += 1
            i += 1
        if cnt > 1:
            total_score += cnt  # 알파벳 순서대로 연속된 개수만큼 점수 추가
        i += 1
    return total_score

T = int(input())
for tc in range(1, T + 1):
    data = input()
    score = cal_score(data)
    print(f'#{tc} {score}')