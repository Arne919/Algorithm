import sys
sys.stdin = open('input.txt')


def horizontal(arr, leng):
    for F in arr:
        for i in range(N-leng+1):
            for j in range(leng//2):
                if F[i+j] != F[i+leng-1-j]:
                    break
            else:
                return True
    return False

for _ in range(10):
    tc = int(input())
    N = 100
    arr1 = list(input() for _ in range(N))
    arr2 = [''.join(x) for x in zip(*arr1)]
    for leng in range(N,1,-1):
        if horizontal(arr1,leng) or horizontal(arr2,leng):
            break
    print(f'#{tc} {leng}')

