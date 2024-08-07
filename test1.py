def solution(progresses, speeds):
    stack =[]
    answer = []
    day = 0
    while True:
        day += 1        # 날짜 추가
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if len(progresses) != 0: # 빈 리스트 될 때까지
            if progresses[0] + speeds[0] * day >= 100:  # 첫번째 작업이 100이상일때
                progresses.pop(0)
                speeds.pop(0)

                count += 1
        # if progresses[i] + speeds[i] * day >= 100: # 작업진도가 100이 넘어갈 때
        #     stack.append(progresses[i])         # stack에 추가
        #     if stack[-1] != progresses[0]:      # 만약 끝낸 작업이 첫번째 작업이 아니라면
        #         progresses.pop(i)               # 작업리스트에서 제외
        #     else:                               # 끝낸 작업이 첫번째 작업일 때
        #         answer.append(len(stack))       # answer에 끝낸작업의 갯수 표시
        #         progresses.pop(i)               # 작업리스트에서 제외
        #         stack.clear()                   # 스택 초기화
        if count > 0:
            answer.append(count)
        else:
            if len(progresses) == 0: # 빈 리스트 되면 break
                break
    return answer
print(solution([93, 30, 55], [1, 30, 5]))