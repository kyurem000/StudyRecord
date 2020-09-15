# 2020-06-20
# 내장함수 : 내장이 되어있기때문에 따로 포트할 필요 없이 바로 사용가능한 함수

# ex) input : 사용자 입력을 받는 함수 

# ex2) dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

# # 방법1------------------------
# print(dir())
# import random # 랜덤은 외장함수 
# print(dir())
# import pickle
# print(dir())

# # 방법2------------------------
# import random
# print(dir(random)) # 랜덤 모듈 내에서 쓸 수 있는 함수들을 표시

# # 방법3------------------------
# lst = [1, 3, 5]
# print(dir(lst)) # 리스트에서 쓸 수 있는 함수들을 표시 

name = "pjy"
print(dir(name)) # 마찬가지로 name이란 문자열에 대해서 쓸 수 있는 함수들을 표시 


# # 방법4------------------------
# list of python builtins 검색 
# https://docs.python.org/ko/3/library/functions.html
# 내장함수에 대해서 설명과 예제가 있다 