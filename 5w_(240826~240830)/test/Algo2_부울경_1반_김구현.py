import sys
sys.stdin = open('algo2_sample_in.txt')

def f(i, N):    # i는 현재 처리 중인 위치, N은 총 외계인 수
    global min_v
    if i == N:   # 모든 외계인 위치를 정했을 때
        s = 0
        # 각 외계인 사이의 위험도를 계산
        for i in range(1, N):
            s += arr[p[i-1]][p[i]]  # 두명 사이의 위험도 합산
        if min_v > s:   # 현재 위험도 합이 더 작은 경우
            min_v = s   # 최소 위험도 업데이트

    else:
        for j in range(i, N):   # 현재 위치 i에 대해 가능한 모든 외계인과 교환
            p[i], p[j] = p[j], p[i]  # p[i]와 p[j] 위치 교환
            f(i+1, N)   # 다음 위치로 이동
            p[i], p[j] = p[j], p[i]  # 원상복구 (백트래킹)

T = int(input())  # 테스트 케이스의 수 입력
for tc in range(1, T+1):  # 각 테스트 케이스 처리
    N = int(input())  # 외계인의 수 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # 위험도 배열 입력
    min_v = 1000  # 위험도의 초기값 설정 (최대값으로 가정)
    p = [i for i in range(N)]  # 외계인의 초기 순서 배열

    f(0, N)  # 재귀 호출을 시작하여 외계인 순서 결정
    print(f'#{tc} {min_v}')  # 결과 출력