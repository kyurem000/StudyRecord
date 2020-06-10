# 2020-06-10
# while문 

custom = "토르"
index = 5
while index >= 1:
    print("{0}, 님의 커피가 준비되었습니다. 다음은 {1}번 입니다.".format(custom, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# 잘못된 코드. 무한 반복 
# coutomer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}".format(coutomer, index))
#     index +=1

customer = "토르"
person = "Unknown"

while person != customer : # 조건에 만족할때까지 문장을 반복된다 
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
