def binary_search_recursive(input_list, low, high, key):
    if low > high:      # 검색이 실패한 경우
        return False
    mid = (low + high) // 2
    if key == input_list[mid]:
        return True
    elif key < input_list[mid]:
        return binary_search_recursive(input_list, low, mid - 1, key)
    elif key > input_list[mid]:
        return binary_search_recursive(input_list, mid + 1, high, key)

num_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]

result = binary_search_recursive(num_list, 0, len(num_list) - 1, 2)