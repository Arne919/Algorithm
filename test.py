import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
student = int(input())
student_arr = [list(map(int, input().split())) for _ in range(student)]


for i in range(student):
    if student_arr[i][0] == 1:          # 남학생인경우
        for j in range(1, (N // student_arr[i][1])+1):  # 숫자의 배수의 스위치
            switch = (student_arr[i][1] * j)-1
            if arr[switch] == 1:
                arr[switch] = 0
            elif arr[switch] == 0:
                arr[switch] = 1
    elif student_arr[i][0] == 2:        # 여학생인경우
        switch = student_arr[i][1]    # 3
        if N//2 >= switch:            #
            j = switch-1                # 2
            if j == 0:         # 3-2-1 =0
                if arr[switch - j] == 1:
                    arr[switch - j] = 0
                else:
                    arr[switch - j] = 1
            else:
                left = arr[switch-j-1:switch] #[0:2] = 01 2-1-1
                right = arr[switch+j:switch:-1]  #[5:3] = 43
                if left == right:
                    for k in range(len(arr[switch-j-1:switch+j])):
                        if arr[switch-j-1+k] == 1:
                            arr[switch-j-1+k] = 0
                        else:
                            arr[switch-j-1+k] = 1
                else:
                    if arr[switch-1] == 1:
                        arr[switch-1] = 0
                    else:
                        arr[switch-1] = 1
        elif N//2 < switch:
            j = N-switch                        # 8-5 = 3
            left = arr[switch-j:switch]         # 5-3 =2:5
            right = arr[switch+j:switch:-1]   #5+3 8:5 8 7 6
            if left == right:
                for k in range(len(arr[switch-j:switch+j+1])):
                    if arr[switch-j+k] == 1:
                        arr[switch-j+k] = 0
                    else:
                        arr[switch-j+k] = 1
            else:
                if arr[switch-1] == 1:
                    arr[switch-1] = 0
                else:
                    arr[switch-1] = 1
        else:
            break
print(*arr)