# 2020-06-11
# 기본값 

# def profile(name, age, lang):
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어 : {2}"\
#         .format(name, age, lang))


# 같은 학교 / 같은 학년,반, 수업일 경우..
print("= = = 기본값을 사용 = = =")
def profile(name, age=17, lang="파이썬"): #age 기본값이 17 , lang 기본값이 파이썬
    # 역슬래시를 넣으면 줄을 바꾸고 이어서 내용을 쓸 수 있다 
    print("이름 : {0}\t나이 : {1}\t 주 사용 언어 : {2}" \
        .format(name, age, lang))

profile("유재석")
profile("김태호")

# 키워드값 =====================
print("= = = 키워드값을 사용 = = =")

def profile2 (names, ages, langs):
    print(names, ages, langs)

profile2(names="유재석", ages=20, langs="파이썬")
profile2(langs="파이썬", names="김태호", ages=20)