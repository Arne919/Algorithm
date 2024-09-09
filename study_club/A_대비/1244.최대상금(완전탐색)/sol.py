import sys
sys.stdin = open('input.txt')

def dfs(lev):
    global result
    # 현재 깊이(스왑 횟수)가 허용된 스왑 횟수와 같으면
    if lev == cnt:
        # ''.join(map(str, num)) <- 리스트 num을 문자열로 변환
        # int(''.join(map(str, num))) <- 변환된 문자열을 정수로 변환
        result = max(result, int(''.join(map(str, num))))   # 최대값 갱신
        return
    # 모든 인덱스 쌍을 반복하며 스왑
    for i in range(L-1):
        for j in range(i+1, L):
            # i와 j 위치의 숫자를 교환
            num[i], num[j] = num[j], num[i]

            # 현재 숫자를 정수로 변환
            change = int(''.join(map(str, num)))
            # 현재 상태(깊이, 숫자)가 방문한 상태 목록에 없는 경우
            if (lev, change) not in visited:
                # 다음 깊이로 재귀 호출
                dfs(lev+1)
                # 이 상태로 방문한 것으로 기록
                visited.append((lev, change))
            # 교환한 요소들 원상복귀
            num[i], num[j] = num[j], num[i]
T = int(input())
for tc in range(1, T + 1):
    N, cnt = input().split()
    cnt = int(cnt)
    num = list(map(int, str(N)))

    L = len(num)
    result = 0
    visited = []
    dfs(0)
    print(f'#{tc} {result}')