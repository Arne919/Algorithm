# def f(n):
#     global cnt
#     cnt+=1
#     if n == 0:
#         return
#     else:
#         f(n-1)
# cnt =0
# f(500)
# print(cnt)

def f(i, N):
    if i == N:
        return
    else:
        print(arr[i])
        f(i+1, N)
        return
arr = [1, 2, 3]
N = 3
f(0, N)