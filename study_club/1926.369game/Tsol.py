# 해결방법 : 3, 6, 9를 카운트 ---> '-'로 출력
# 1. count 메서드 사용 하면 쉽게 풀 수 있다.
# 2. count 메서드 사용 금지

# 첫 번째 방법 : count 메서드 사용
'''
number = int(input())
for num in range(1, number + 1):
    num = str(num)
    clap = num.count('3') + num.count('6') + num.count('9')

    if clap == 0:
        print(num, end = ' ')
    else:
        print('-' * clap, end = ' ')
'''
# 두 번째 방법 : 직접 카운팅
'''
def game_369(N):
    result = []
    for i in range(1, N + 1):
        num_str = str(i)
        cnt = 0
        for digit in num_str:
            if digit in ['3', '6', '9']:
                cnt += 1
        if cnt > 0: # 박수
            result.append('-' * cnt)
        else:
            result.append(num_str)
    return result

N = int(input())
print(*game_369(N))
'''
# 1220 magnetic


# 세로 라인 검사
'''
def get_sero_cnt(col):
    cnt = 0
    is_red = False

    for row in range(N):
        if arr[row][col] == 1: # red 발견시
            is_red = True
        elif is_red and arr[row][col] == 2: # 레드를 발견했었고, 현재 blue를 발견했다
            cnt += 1
            # is_red = False # 갱신
    return cnt

for tc in range(1, 2):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for col in range(N):
        result += get_sero_cnt(col)
    print(f'{tc} {result}')

'''
# 히든 테케가 100개 ---> 채점
# 100개의 테스트케이스 중에 98개 통과 ---> fail
# 결론 함수를 만들면 가독성좋아진다 ---> 디버깅에 용이!!!!!
