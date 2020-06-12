# 2020-06-09
# # 규칙 1  http://  부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성


url = "http://naver.com"
#규칙1
my_str = url.replace("http://", "") 

# 규칙2
my_str = my_str[ : my_str.index(".")] # my_str 변수에 있는 문자열 중에서 처음 나오는 . 의 위치 직전까지 

# 규칙3
password = my_str[:3] + str(len( my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀 번호는 {1} 입니다.".format(url, password))