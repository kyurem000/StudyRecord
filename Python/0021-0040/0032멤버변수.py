# 2020-06-12
# 멤버변수 

# 여기서 멤버 변수란 self."name" , self."hp" , self."damage" 가 됨 

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
# 변수 이름 . (점) 을 쓰면 쓸 수 있는 멤버변수가 나온다 
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마컨 
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True
# 클로킹이란 변수는 클래스 내부에 없다
# 외부에서 클로킹이란 변수를 추가로 할당한 것
# 파이썬에서는 어떤 객체에 추가로 변수를 외부에서 만들어서 쓸 수 있다 

# 확장된 변수는 내가 확장을 한 객체에 대해서만 적용이되고
# 기존에 있던 다른 객체에는 적용이 안된다.
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))