#2020-06-08
# 슬라이싱 
sentence = '나는 문자열이다'
print(sentence)
sentence2 = "나는 파이썬이다"
print(sentence2)
sentence3 = """
나는
문자열이고
파이썬이다
"""
print(sentence3)


jump = "980908-1234567"
        # 0부터 시작 

#문자열 가져오기 
print("성별 : " + jump[7] ) # 0번째를 기준으로 7번에 있는 문자열을 가져온다
print("연 : " + jump[0:2] ) # 0번째 부터 2번째 직전 까지 값을 가져온다
print("월 : " + jump[2:4] ) # 2, 3번째 값을 가져온다 
print("일 : " + jump[4:6] )
print("생년월일 : " + jump[:6]) # 처음부터 6 직전까지 값을 가져온다 
print("뒤 7자리 : " + jump[7:]) # 7부터 끝까지 값을 가져온다
print("뒤 7자리 (뒤에부터) : " + jump[-7:]) # 맨 뒤에서 7번째부터 끝까지 값을 가져온다