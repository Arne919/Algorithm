# list = [1,2,3]
# print(len(list))
# for i in range(len(list)):
#     print(i)


def solution(progresses, speeds):
    N = len(progresses)
    answer = []
    day = 0

    while progresses:  # progresses가 비어있지 않을 때까지 반복
        day += 1  # 날짜 추가
        completed_count = 0  # 완료된 작업의 수

        # 진행 상황을 업데이트하고 완료된 작업을 체크
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 완료된 작업 수 세기
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            completed_count += 1

        # 완료된 작업이 있으면 결과에 추가
        if completed_count > 0:
            answer.append(completed_count)

    return answer


# 테스트
print(solution([93, 30, 55], [1, 30, 5]))  # 예상 출력: [2, 1]
