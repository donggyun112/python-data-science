ft_list = ["Hello", "tata!"]  # 리스트
ft_tuple = ("Hello", "toto!")  # 튜플
ft_set = {"Hello", "tutu!"}  # 집합 순서가 없기 때문에 index로 접근할 수 없다
ft_dict = {"Hello": "titi!"}  # 딕셔너리
# 리스트와 집합의 차이는 중복을 허용하는가 여부이다. 리스트는 중복을 허용하지만 집합은 중복을 허용하지 않는다.
# index로 접근할 수 있는 리스트와 달리 집합은 index로 접근할 수 없다.

ft_list.remove("tata!")
ft_list.append("World!")
# 튜플은 수정이 불가능하다.
# 따라서 리스트로 변환 후 수정해야 한다.
# 튜플 주소 출력
# print(id(ft_tuple))
ft_tuple_list = list(ft_tuple)
ft_tuple_list.remove("toto!")
ft_tuple_list.append("Korea!")
ft_tuple = tuple(ft_tuple_list)
# print(id(ft_tuple))
# id값이 다르게 변경됨
# 결국 새로운 튜플을 생성한 것

ft_set.remove("tutu!")
ft_set.add("Seoul!")
# 집합은 순서가 보장되지 않는 특성이 있다.

ft_dict["Hello"] = "42Seoul!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
