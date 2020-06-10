# 2020-06-08
# 문자열처리함수 
python = "Python is Amazing"

print(python.lower()) # 모두 소문자로
print(python.upper()) # 모두 대문자로 
print(python[0].isupper()) # 이 문자열이 대문자가 맞는가 맞으면 True 틀리면 False
print(len(python)) # 문자열의 길이 측정 
print(python.replace("Python", "JAVA")) # Python이란 문자열을 JAVA로 바꾼다 

index = python.index("n") # n이란 문자열이 몇번째 위치에 있나 찾기 
print(index)

index = python.index("n", index + 1)  # 앞에서 찾은 위치 그 다음부터 찾는다, 앞에 찾은 5라는 위치부터 다음을 찾는다, 따라서 2번째 n의 위치를 찾는다
print(index)

print(python.find("n")) # n이란 문자열의 위치를 찾는다, 값이 아예 없을 경우 -1을 반환하고 프로그램은 진행한다
# print(python.index("Java")) # python이란 변수에는 Java라는 문자열이 없기때문에 오류를 내보내고 프로그램을 중지한다 

print(python.count("n")) # n이 총 몇 번 나왔는지 출력 