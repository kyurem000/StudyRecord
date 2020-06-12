# 2020-06-12
# 지역변수와 전역변수 

# 전역변수 : 모든 공간내에서 어디서든지 부를 수 있는 변수
# 지역변수 : 함수내에서만 쓸 수 있는 변수 (함수 호출이 끝나면 사라지는 변수 )

# = = = 방법1 = = =
gun = 10
def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun을 사용한다는 뜻 ( 8행에 있는 gun )
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    
    
# = = = 방법2 = = =
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무를 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))