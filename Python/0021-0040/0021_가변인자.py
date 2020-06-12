# 2020-06-11
# *가변인자
# 서로 다른 개수의 값을 넣어줄때는 가변인자(*로 시작하는 매개변수)를 이용해서 활용할 수 있다 

# def profile(names="유재석", age=20, lang1, lang2, lang3, lagn4, lang5):
#     print("이름 : {0}\t나이 : {1}\t"\
#     .format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# \t 는 문자열 사이에 탭 간격을 줄 때 사용 한다 

# end 라는것을 정의하면 이 프린트문이 끝날때 줄바꿈을 하지않고 이렇게만 끝난다

def profile(name, age, *language):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")