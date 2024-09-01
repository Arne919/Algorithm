def find_repeat_word():
    # 스택으로...
    stack = []
    for i in range(len(string)):
        if stack and stack[-1] == string[i]:
            stack.pop()
            # 인덱스 에러 오지게 남 깨달음
            if i < len(string) - 1 and string[i] == string[i + 1]:
                stack.append(string[i])
        else:
            stack.append(string[i])
    cnt = len(string) - len(stack)
    return stack, cnt


# 연속 숫자 체크
def count_num(lst):
    c_num = 1
    result = 0
    for i in range(len(lst) - 1):
        if lst[i] + 1 == lst[i + 1]:
            c_num += 1
        else:
            if c_num > 1:
                result += c_num
                c_num = 1
    else:
        if c_num > 1:
            result += c_num
    return result


T = int(input())
for tc in range(1, T + 1):
    string = input()
    new_str, count = find_repeat_word()

    # 가공된 문자열 숫자로 다 바꿔주기
    num_lst = []
    for c in new_str:
        num_lst.append(ord(c))
    # 연속 숫자 세주고 더해주기
    count += count_num(num_lst)
    # 악랄하다 문제가
    print(f'#{tc} {count}')