# 2020-06-11

# 함수 선언 
# def 함수이름(전달하려는 값) : 
# def open_account() :

# 함수의 호출 
# open_account()


def open_account() :
    print("새로운 계좌가 생성되었습니다.")

# 입금
def deposit(balance, money): 
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다. ".format(balance + money))
    return balance + money # 반환 

# 출금
def witdraw(balance, money): 
    if balance >= money: #잔액이 출금보다 많으면.. 출금할 금액 > 잔액 
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

# 저녁시간에 출금 
def witdraw_night(balance, money):
    commission = 100 # 수수료 100원 
    return commission, balance - money - commission # 두 개의 값을 콤마로 구분해서 튜플 형식으로 보내준다 

# 잔액 
balance = 0
balance = deposit(balance, 1000)
# balance = witdraw(balance, 500)
commission, balance = witdraw_night(balance, 500) # balance와 출금하고싶은 금액 500원
print("수수료는 {0}원 이며, 잔액은 {1}원 입니다.".format(commission, balance))
