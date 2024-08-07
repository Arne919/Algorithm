def solution(progresses, speeds):
    answer = []

    while True:  # progresses가 비어있지 않을 때까지 반복
        cnt = 0  # 완료된 작업의 수


        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        for i in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1

        if cnt > 0:
            answer.append(cnt)
        else:
            if len(progresses) == 0:
                break

    return answer

# 테스트
print(solution([93, 30, 55], [1, 30, 5]))  # 예상 출력: [2, 1]
