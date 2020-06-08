# 2020-06-08
# 문자열, 랜덤 함수 
from random import *

print( random() ) # 0.0 dltkd ~ 1.0 "미만"의 임의의 값 생성 
print( random() * 10 ) # 0.0 ~ 10.0 "미만"의 임의의 값 생성 
print( int ( random () * 10 ) ) # 0 ~ 10 "미만"의 임의의 값 생성 
print( int ( random () * 10 ) +1 ) # 1 ~ 10 "이하"의 임의의 값 생성 
print ( int ( random () * 45 ) +1 ) # 1 ~ 45 "이하"의 임의의 값 생성 
print ( randrange (1, 46) ) # 1 ~ 46 "미만"의 임의의 값 생성 
print ( randint (1, 45) ) # 1 ~ 45 "이하"의 임의의 값 생성 


# 문제1
a = randint(1, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(a) + "일로 선정되었습니다.")