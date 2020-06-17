# 2020-06-17
# 모듈 : 어떤 필요한 것끼리 부품처럼 만들어진 파일
# 함수정의나 클래스정의 등의 파이썬 문장들을 담고있는 파일을 "모듐" 이라고한다. 
# 모듈의 확장자는 .py 이다 


# --------------------------------------------------이것이 모듈파일이 된다
# 일반 가격
def price(people):
    print("{0} 명 가격은 {1}원 입니다.".format(people, people * 10000))


# 조조할인 가격
def price_morning(people):
    print("{0} 명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))
    

# 군인 할인 가격
def price_soldier(people):
    print("{0} 명 군인 할인 가격 가격은 {1}원 입니다.".format(people, people * 4000))

