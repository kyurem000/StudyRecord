# 2020-06-12 
# class 

# 마린 : 공격 유닛, 총을 쏠 수 있음
# name = "마린" # 이름
# hp = 40 # 체력 
# damage = 5 # 공격력 
# print(" {} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 두 모드가 있음
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print(" {} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# # 함수 
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# # 이럴떄 필요한 것이 클래스 

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