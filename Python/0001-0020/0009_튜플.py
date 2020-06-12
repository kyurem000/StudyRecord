# 2020-06-10
# 튜플은 리스트와 유사하나 내용을 바꿀 수 없지만 더 적은 자원을 사용하기 때문에 비교적 가볍다.


menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# 이렇게 선언한 것을 
# name = "김종국"
# age = 20
# hobby = "coding"
# print(name, age,  hobby)


# 튜플을 이용해서 선언한다면 
(name, age, hobby) = ("김종국", 20, "coding")
print(name, age, hobby)
