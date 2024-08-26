arr = [1,2,3,4]
N=4
def f(i, N, v):
    if i == N:
        return 0
    if arr[i] == v:
        return 1
    else:
        return f(i+1, N, v)
print(f(0,N,6))