# DATA = [0, 4, 1, 3, 1, 2, 4, 1]
# COUNTS = [0] * 5    # DATA가 0~4까지의 정수
#
# N = len(DATA)       # DATA의 크기
# TEMP = [0] * N      # 정렬 결과 저장
#
# # 1단계 : DATA 원소 별 개수 세기
# for x in DATA:      # DATA의 원소 x를 가져와서 COUNTS[x]에 개수 기록
#     COUNTS[x] += 1
#
# # 2단계 : 각 숫자까지의 누적 개수 구하기
# for i in range(1, 5):       # COUNTS[1] ~ COUNT[4]까지 누적개수
#     COUNTS[i] = COUNTS[i-1] + COUNTS[i]
#
# # 3단계 : DATA의 맨 뒤부터 TEMP에 자리 잡기
# for i in range(N-1, -1, -1):
#     COUNTS[DATA[i]] -= 1    # 누적개수 1개 감소
#     TEMP[COUNTS[DATA[i]]] = DATA[i]
#
# print(*TEMP)

#------------------------------------------------------------
import sys
sys.stdin = open('input.txt')

def counting_sort(input_arr, k):
    '''
    input_arr: 입력배열(1 to k)
    counting_arr: 카운트 배열
    k는 데이터의 개수가 아닌 데이터 원소의 범위
    '''

    counting_arr = [0] * (k)
    # print(1, counting_arr)

    # 1. counting_arr에  arr내 원소의 빈도수 담기
    for i in range(len(input_arr)):
        counting_arr[input_arr[i]] += 1
    # print(2, counting_arr)


    # 2. 누적(counting_arr 업데이트)
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i-1]
    # print(3, counting_arr)


    # 3. result_arr 생성
    result_arr = [-1] *  len(input_arr)
    # print(4, result_arr)


    # 4. result_arr에 정렬하기(counting_arr를 참조)
    for i in range(len(result_arr)-1, -1, -1):
        counting_arr[input_arr[i]] -= 1
        result_arr[counting_arr[input_arr[i]]] = input_arr[i]
    # print(5, result_arr)

    return result_arr
a = [0, 4, 1, 3, 1, 2, 4, 1]
# a = list(map(int(input().split(','))))
print(counting_sort(a,5))