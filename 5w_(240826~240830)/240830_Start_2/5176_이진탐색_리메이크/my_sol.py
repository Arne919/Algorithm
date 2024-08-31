import sys
sys.stdin = open('input.txt')

# 리스트를 중위순회대로 완전 이진 트리에 맞게 입력하는 함수
def inorder(password, tree, a=1):
    if a < len(tree):  # 인덱스가 트리의 길이보다 작을 때만 진행
        inorder(password, tree, 2*a)    # 왼쪽 자식 방문
        # 현재 노드에 값 할당
        if password:  # 비어 있지 않을 때만 pop
            tree[a] = password.pop(0)
        inorder(password, tree, 2*a+1)  # 오른쪽 자식 방문

T = int(input())
for tc in range(1, T+1):
    secret = input().strip()
    salt = int(secret[0])   # 첫번째 숫자 salt
    hex_str = secret[1:]    # 나머지 16자리 16진수 문자열
    
    # 16진수(2자리씩) -> 10진수
    dec_str = []
    for i in range(0, 16, 2):
        hex_pair = hex_str[i:i+2]   # 2자리 끊기
        dec_num = int(hex_pair, 16) # 16->10진수
        dec_str.append(dec_num)     # 10진수 리스트에 추가
    
    # 각 인덱스마다 salt값 빼기
    result = []
    for i in range(8):
        new_salt = (i+1) * salt         # 인덱스별 salt 값 변환
        result.append(dec_str[i] - new_salt)

    # 오름차순 정렬
    result.sort()

    # 각 숫자의 1의 자리수만 뽑아서 비번생성
    password = []
    for i in result:
        last_str = i % 10
        password.append(str(last_str))
    # print(password)

    # 완전 이진 트리를 저장할 리스트, 인덱스 1부터 사용
    tree = [None] * 9
    inorder(password, tree) # 완전이진트리로 배치된 중위순회 함수
    # 완전 이진 트리에 맞게 출력
    final = ''
    for i in range(1, 9):
        final += str(tree[i])
    print(f'#{tc} {final}')