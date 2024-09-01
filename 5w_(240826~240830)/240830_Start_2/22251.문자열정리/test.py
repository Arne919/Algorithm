import sys
sys.stdin = open('input.txt')

def alph(char1, char2):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    idx1 = alphabet.index(char1.lower())
    idx2 = alphabet.index(char2.lower())
    # char2가 char1의 다음 문자인지 확인
    return idx2 == idx1 + 1

def cal_score(data):
    total_score = 0
    while True:
        new_str = []
        i = 0
        score = 0
        while i < len(data):
            cnt = 1
            while i+1<len(data) and data[i] == data[i+1]:
                cnt += 1
                i += 1
            if cnt > 1:
                score += cnt
            else:
                new_str.append(data[i])
            i += 1
        if score == 0:
            break
        total_score += score
        data = ''.join(new_str)
    i = 0
    while i < len(data)-1:
        cnt = 1
        while i+1<len(data) and alph(data[i], data[i+1]):
            cnt+=1
            i+=1
        if cnt > 1:
            total_score += cnt
        i+=1
    return total_score


T = int(input())
for tc in range(1, T+1):
    data = input()
    score = cal_score(data)
    print(f'#{tc} {score}')