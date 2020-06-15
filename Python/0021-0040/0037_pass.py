# 2020-06-15
# pass

# 2020-06-13
# 메소드 오바리이딩 

# 일반 유닛 
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name # 여기서 name이란 위에서 전달받은 name을 뜻함
        self.hp = hp
        self.speed = speed

    def move(self, location): # 메소드 오버라이딩 
        print("[지상 유닛 이동]")
        print(" {0} : {1} 방향으로 이동합니다. [속도 {2}] ".format(self.name, location, self.speed))
# self란 자기 자신을 뜻함. 클래스 내에서 메소드 앞에는 항상 self를 적어줘야한다.

# 상속은 말 그대로 물려받는 것을 이야기함. 괄호안에 내가 상속받고싶은 클래스를 적는다
# 유닛에 있는 멤버변수를 어택유닛에서 쓸 수 있게 되었다 

# 다중 상속이란? 부모가 둘 이상인 상속을 말함 
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) #
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
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [ 속도 {2} ]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스 
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0으로 처리 
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 메소드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# pass 설명 추가-------------------------------------------------------

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무것도 안하고 일단 넘어간다 , 완성된거처럼 보일 수 있다 

# 서플라이 : 건물, 1개 건물 = 8개의 유닛 
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다. ")

def game_over():
    pass

game_start()
game_over()
    
