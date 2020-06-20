# 2020-06-15
# 스타크래프트 프로젝트 전반전 

from random import * 
# 일반 유닛 
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name # 여기서 name이란 위에서 전달받은 name을 뜻함
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다. ".format(name))

    def move(self, location): # 메소드 오버라이딩 
        print("[지상 유닛 이동]")
        print(" {0} : {1} 방향으로 이동합니다. [속도 {2}] ".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 유닛이 파괴되었습니다.".format(self.name))

# 공격 유닛 
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) #
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
# 마린 
class Marine(AttackUnit):
    def __init__(self):
       AttackUnit.__init__(self, "마린", 40, 1, 5)

# 스팀팩 : 체력10 감소하고 일정시간 동안 이동속도, 공격속도 증가 
    def stimpack(self):
        if self.hp >10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} 체력이 부족하여 스팀팩을 사용하지 않습니다. ".format(self.name))
        
# 탱크
class Tank(AttackUnit):
        # 시즈모드 : 더 높은 파워로 공격이 가능해짐, 이동 불가 
    seize_mod = False # 시즈모드 개발 여부 

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mod = False

    def set_seize_mod(self):
        if Tank.seize_mod == False:
            return 

    # 현재 시즈모드가 아닐 때  -> 시즈모드
        if self.seize_mod == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mod = True
    # 현재 시즈모드 일 때  -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mod = False



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
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: #클로킹 모드 -> 모드 해제
            print("{0} 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False 
            
        else : # 클로킹 모드 해제 -> 모드 설정
            print(" {0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True 

def game_start():
    print("[알림] 새로운 게임을 시작힙니다.")

def game_over():
    print("Player : GG")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 시작 
game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크
t1 = Tank()
t2 = Tank()

# 레이스 
w1 = Wraith()

attack_units = [ ]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_mod = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹 )
# * 새로 나온 인스턴스 ---------------------------------------------
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mod()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해 입음
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 (5 ~ 20)
    
# 게임 종료 
game_over()