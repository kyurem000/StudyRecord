# 2020-06-12
# Quiz

# 표준 체중을 구하는 프로그램을 작성하시오
# * 표중 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#     남자 : 키(m) x 키 (m) x 22
#     여자 : 키(m) x 키 (m) x 21

# 조건1) 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2) 표준 체중은 소수점 둘째자리까지 표시

# 출력예제) 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender): # 키 m 단위(실수), 성별은 문자열이므로 str
    if gender == "남자":
        return height * height * 22
    elif gender == "여자":
        return height * height * 21

height = int(input(" 키를 입력해주세요. "))
gender = str(input(" 성별을 입력해주세요. "))
weight = round(std_weight(height / 100, gender),2) # 위 함수에서 단위가 m이기때문에 100으로 나눔
# round 함수를 이용해서 소수점 둘째짜리만 표시함 

print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(height, gender, weight))