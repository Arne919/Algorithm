# 방향배열 어떻게 응용되면 어렵나?? 물론 im에서 완전탐색X 백트래킹 X
# continue, break 쓰는 경우
# if 0 <= ny < N and 0 <= nx < N:

# break

lst = [1, 2, 3, 4, 5]
for i in lst: # i = 1, 2, 3, 4, 5
    if i == 3: # i = 1일때 print(1), i = 2일때 print(2), i = 3일때 break ---> 반복문 탈출, 종료
        break 
    print(i) # 출력 결과 1 2

for i in lst:
    if i == 3: # i = 3일때 print가 되지 않고 반복문의 처음으로 돌아간다. 
        continue
    print(i) # 출력 결과 1 2 4 5