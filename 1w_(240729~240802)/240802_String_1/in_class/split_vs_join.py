"""
- split()
    - 문자열 -> 리스트로 변환을 한다.
    - 파라미터(구분자)를 기준으로 나누어서 리스트에 넣는다.

- join()
    - 리스트 -> 문자열로 변환
    - iterable ( 반복가능한, 순회가능한)
                 객체 요소들을 하나의 문자열로 변환 )
"""
str_example = "hello333world"
new_example = str_example.split('333')
# print(str_example)
# print(new_example)

list_example = ["hello", "world", "!!!!"]

result_1 = ''.join(list_example)
print(result_1)

result_2 = ",".join(list_example)
print(result_2)

result_3 = "&&&".join(list_example)
print(result_3)
