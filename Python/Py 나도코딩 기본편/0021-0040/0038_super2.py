# 2020-06-15
# super 

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Fylable:
    def __init__(self):
        print("Flyable 생성자")

# class FlyableUnit(Unit, Fylable):
#     def __init__(self):
#         super().__init__()

# class FlyableUnit(Fylable, Unit):
#     def __init__(self):
#         super().__init__()

# * super를  쓰면 순서상에 맨 마지막에 상속받는 클래스에 대해서만 함수가 호출이된다

# 다중상속을 할때는, 모든 부모 클래스에 대해서 초기화가 필요하다하면 따로 명시적으로...
class FlyableUnit(Fylable, Unit):
    def __init__(self):
        Unit.__init__(self)
        FlyableUnit.__init__(self)
        # 이런식으로 두 번을 통해서 초기화를 하는 방식을 사용할 수 있다 

# 드랍쉽
dropship = FlyableUnit()