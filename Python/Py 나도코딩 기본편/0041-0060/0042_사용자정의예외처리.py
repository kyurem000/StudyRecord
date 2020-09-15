# 2020-06-15
# 사용자 정의 예외처리 
# finally

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
try:
    print("한 자리 숫자 나누기 전용 계산기입니다")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    if num1 >= 10 or num2 >= 10: # 10보다 같거나 크면  
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 사용자가 정의한 예외처리,
# 18행에서 에러가 발생하였을때 우리가 정의한 메세지를 던져주고
# 빅넘버메세지에서는 메세지를 가지고있다가 23행 메세지를 받아와서 출력해준다
    print("{0} / {1} = {2} ".format(num1,num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
#-------------------finally 설명 추가--------------------
# 예외처리 구문중에서 정상적으로 처리가 되던 오류가 발생하건 상관없이 "무조건" 실행되는 구문이다.
finally:
    print("계산기를 이용해 주셔서 감사합니다.")

