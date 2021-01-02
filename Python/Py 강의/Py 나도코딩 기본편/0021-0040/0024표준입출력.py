# 2020-06-12
# 표준입출력

#지금까지는 
print("python1", "java1") # 이렇게 했지만 
print("=====")

# sep를 넣으면 콤마부분에 특정문장을 넣을 수 있다 
print("python", "java", sep=" vs ") 
print("=====")

# end부분을 명시적으로 적어주게되면 연달아서 한 줄로 나온다.
print("c", "c++", "c#", sep=",", end="?")
print("어떤 언어가 제일 재밌을까")
print("=====")

import sys
print("HTML", "CSS", "JS", file=sys.stdout) # stdout은 표준출력으로 문장이 찍히는 것
print("HTML", "CSS", "JS", file=sys.stderr) # stderr은 표준에러로 처리되어서 찍히는 것 

# 예제1 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score) # 우리가 기본적으로 출력했던 부분 
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # ljust 란? l은 left를 의미, 왼쪽으로 정렬을 하는데 총 8칸의 공간을 확보한 상태에서 정렬해달라는 뜻 
    # rjust 란? r은 right를 의미, 오른쪽정렬을 하는데 총 4칸의 공간을 확보한 상태에서 정렬해달라는 뜻 

#  예제2 은행 대기순번표
# 001, 002, 003....
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # zfill 란? 0을 채우는것,  3크기만큼의 공간을 확보를 하고 값을 넣는데 값을 없는 곳엔 0으로 채워달란 뜻 


# 표준 입력에 대해서..
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은" + answer + "입니다.")
# 사용자 입력을 통해서 값을 받을땐 항상 "문자열 형태"로 저장된다
