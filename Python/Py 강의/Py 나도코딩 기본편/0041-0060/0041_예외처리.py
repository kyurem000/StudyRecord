# 2020-06-15
# 예외 처리 (exception)

print("= = = 예외 처리 = = =")
try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번쨰 숫자를 입력해주세요.")))
    nums.append(int(input("두 번째 숫자를 입력해주세요.")))
    nums.append(int(nums[0] / nums[1])) # 이 부분을 깜빡한다면? 에러가 난다
    print("{0} / {1} = {2} ".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("[에러] 숫자를 입력해주세요.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

# 에러 발생시키기 
print("= = = 에러 발생시키기 = = =")
try:
    print("한 자리 숫자 나누기 전용 계산기입니다")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    if num1 >= 10 or num2 >= 10: # 10보다 같거나 크면  
        raise ValueError
    print("{0} / {1} = {2} ".format(num1,num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")