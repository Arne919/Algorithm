def solution(progresses, speeds):
    N = len(progresses)
    stack = []
    answer = []
    day = 0
    while True:
        day += 1        # 날짜 추가
        for i in range(N):
            if progresses[i] + speeds[i] * day >= 100: # 작업진도가 100이 넘어갈 때
                stack.append(progresses[i])         # stack에 추가
                if stack[-1] != progresses[0]:      # 만약 끝낸 작업이 첫번째 작업이 아니라면
                    progresses.pop(i)               # 작업리스트에서 제외
                else:                               # 끝낸 작업이 첫번째 작업일 때
                    answer.append(len(stack))       # answer에 끝낸작업의 갯수 표시
                    progresses.pop(i)               # 작업리스트에서 제외
                    stack.clear()                   # 스택 초기화
        else:
            if len(progresses) == 0:
                break
    return answer