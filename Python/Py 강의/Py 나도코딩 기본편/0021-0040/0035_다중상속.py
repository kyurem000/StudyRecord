# 2020-06-13
# 다중 상속 

# 일반 유닛 
class Unit:
    def __init__(self, name, hp):
        self.name = name # 여기서 name이란 위에서 전달받은 name을 뜻함
        self.hp = hp
# self란 자기 자신을 뜻함. 클래스 내에서 메소드 앞에는 항상 self를 적어줘야한다.

# 상속은 말 그대로 물려받는 것을 이야기함. 괄호안에 내가 상속받고싶은 클래스를 적는다
# 유닛에 있는 멤버변수를 어택유닛에서 쓸 수 있게 되었다 

# 다중 상속이란? 부모가 둘 이상인 상속을 말함 
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

# 드랍쉽 : 공중 유닛
# 날 수 있는 기능을 가진 클래스 
class  Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [ 속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스 
class  FlyAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리
valkyrie = FlyAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
    
