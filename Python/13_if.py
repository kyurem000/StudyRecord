# 2020-06-10
# if 문 

# weather = input("오늘 날씨는 어때요?") # input은 사용자에게 입력 받는 것
# if weather == "비" or weather == "눈" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 꼭 챙기세요")
# else :
#     print("준비물이 필요 없습니다")

temp = int(input("기온은 어때요?")) # 입력받은 값을 정수형으로 바꿔줌 

if 30 <= temp : # 30보다 같거나 크면 조건
    print("너무 더운 날씨입니다. 나가지 마세요.")
elif 10 <= temp and temp < 30 : # 10보다 같거나 크면서 30보다 작아야하는 조건 
    print("괜찮은 날씨 입니다.")
elif 0 <= temp < 10 :
    print("외투를 챙기세요.")
else :
    print("너무 추워요. 나가지 마세요.")