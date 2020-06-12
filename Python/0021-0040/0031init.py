# 2020-06-12
# init

# __init__ 이 부분은 파이썬에서 쓰이는 생성자
# 마린이나 탱크와 같이 "객체"가 만들어질때 자동으로 호출되는부분 
#객체 마린이나 탱크와 같이 클래스로부터 만들어지는 녀석들을 "객체"라고함
# 이때 마린과 탱크는 Unit 클래스의 인스턴스 라고 표현한다 
# 객체가 생성될때는 기본적으로 이미 함수에 정의된 개수와 동일하게 해야함
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린") # 오류. 함수에 정의된 개수만큼 보내주지 못해서 오류가 남 