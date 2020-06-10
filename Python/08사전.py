# 2020-06-10
#  사전 

cabinet = { 3:"유재석", 100:"김태호"} # 열쇠가 3 주인이 유재석, 열쇠가 100, 주인이 김태호 

print(cabinet[3]) # 유재석 
print(cabinet[100]) # 김태호

print(cabinet.get(3)) # 유재석 
# print(cabinet[5]) # 없는 키이기 때문에 오류가 나서 프로그램이 종료가 되었다. 뒤에 hi는 실행이 안되었다
# print(" 위에서 프로그램이 종료가 되었기 떄문에 이 부분부터는 실행되지 않는다 ")

print(cabinet.get(5)) # get은 없는 키가 출력되도 프로그램이 종료되지 않고 진행된다.
print(" get 이라서 없는 key지만 프로그램이 종료되지 않았다")
print("==================")

print(cabinet.get(5, "key 5의 내용이 대체됨")) # 5라는 key 값을 찾고, 없다면 "대체제" 라는 문자열이 출력되게끔 한다 
print(" 5라는 key가 없지만 내용이 대체되었다 ")
print("==================")

print ( 3 in cabinet ) # 3이라는 키가 cabinet에 있느냐? -> TRUE
print ( 50 in cabinet ) # 50이라는 키가 cabinet에 있느냐? -> FALSE
print("==================")

#정수가 아닌 문자열로도 key를 지정해줄 수 있다 
car2 = {"A-3":"홍길동", "B-20":"동길홍"}
print(car2["A-3"])
print(car2["B-20"])

print("==================")

# 새로운 손님
print(car2)
car2["A-3"] = "김종국"
car2["B-20"] = "조세호"
print(car2)
print(" 홍길동 자리에 김종국이 앉았다 ")
print("==================")

# 간 손님
del car2["A-3"] # A-3에 해당하는 값은 지워진다
print(car2)
print(" A-3에 해당하는 값이 지워졌다 ")
print("==================")

# key 들만 출력
# keys 사용 
print(car2.keys())

# value 들만 출력
# values 사용 
print(car2.values())

# key와 value 둘 다 출력 
# itme 사용 
print(car2.items())