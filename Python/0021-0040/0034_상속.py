# 2020-06-13
# 상속 

# 일반 유닛 
class Unit:
    def __init__(self, name, hp):
        self.name = name # 여기서 name이란 위에서 전달받은 name을 뜻함
        self.hp = hp
# self란 자기 자신을 뜻함. 클래스 내에서 메소드 앞에는 항상 self를 적어줘야한다.

# 상속은 말 그대로 물려받는 것을 이야기함. 괄호안에 내가 상속받고싶은 클래스를 적는다
# 유닛에 있는 멤버변수를 어택유닛에서 쓸 수 있게 되었다 
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) #
        self.damage = damage
        

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 유닛이 파괴되었습니다.".format(self.name))

# 파이어뱃
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
#공격을 2번 받는다고 가정 
firebat1.damaged(25)
firebat1.damaged(25)

