import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    V, E = map(int, input().split())
    adjl = [[] for _ in range(V+1)]
    visited = [True for _ in range(V+1)]
    arr = list(map(int, input().split()))
    cnt = V

    for i in range(E):
        a, b = arr[i*2], arr[i*2+1]
        adjl[b].append(a)
    result = []
    while cnt:
        for i in range(1, len(adjl)):
            if visited[i]:
                for j in adjl[i]:
                    if visited[j]:
                        break
                else:
                    visited[i] = False
                    result.append(i)
                    cnt -= 1


    print(f'#{tc} ', end='')
    print(*result)