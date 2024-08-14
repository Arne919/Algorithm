'''
String vs List
공통점
- iterable 하다. 순회 가능하다는 거다. (for loop).
- String도 List라고 생각하면서 사용하자.
- 인덱싱이나 슬라이싱이 가능하다.
(인덱싱: 인덱스로 접근하는거죠. List_example[3] => str_example[3]
슬라이싱: 잘라서 부분만 가져오는거죠. List_example[2:3] => str_example[2:3])
차이점
- String: immutable(불변), List: mutable(가변)
- String: 각 요소를 변경할 수 없어요.
수정하려면 새로운 문자열을 생성해야 한다.
- List: mutable
각 요소를 변경할 수 있고, 수정시 원본이 수정된다.
'''
# String: 각 요소를 변경할 수 없다.
str_example = 'Hello'
# str_example[0] = 'J'
new_example = str_example + 'World'
print(str_example)
print(new_example)

list_example = [1, 2, 3, 4, 5]
list_example[0] = 10
print(list_example)
list_example.append(6)
print(list_example)