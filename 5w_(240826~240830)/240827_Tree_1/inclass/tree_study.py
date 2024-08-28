# '''
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# '''
#
# # left, right 를 쓰는 버전
# # 단, 입력이 반드시 각 노드당 최대 2번식만 들어온다고 가정한 코드
# # 전위 순회(나->왼쪽->오른쪽)
# def preorder(node):
#     if node == 0:
#         return
#     print(node, end=' ')    # 본인을 먼저 확인(전위순회)
#     preorder(left[node])
#     # print(node, end=' ')  # 왼쪽을 보고나서, 본인을 확인(중위순회)
#     preorder(right[node])
#     # print(node, end=' ')  # 왼쪽,오른쪽 자식들을 모두 보고나서, 본인을 확인(후위순회)
#
# N = int(input())            # 정점의 개수(정점: 1~N번)
# arr = list(map(int, input().split()))
# left = [0] * (N + 1)    # 왼쪽 자식 번호를 저장할 리스트
# # ex) left[3] = 2 => 3번 부모의 왼쪽 자식은 2이다
# right = [0] * (N + 1)   # 오른쪽 자식 번호를 저장할 리스트
#
# for i in range(0, len(arr), 2):
#     parent, child = arr[i], arr[i+1]
#
#     # 왼쪽 자식이 없다면, 왼쪽에 삽입
#     if left[parent] == 0:
#         left[parent] = child
#     # 왼쪽 자식은 있는데, 오른쪽 자식이 없다면, 오른쪽에 삽입
#     else:
#         right[parent] = child
#
# root = 1                # 시작점1
# preorder(root)
