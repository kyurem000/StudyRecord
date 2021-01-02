# 2020-06-10
# 한 줄 for 문

# 출석번호가 1,2,3,4,5.... 앞에 100을 붙이기로 함 -> 101,102,103,104,105....
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # i에다가 100을 더한 값을 sudents라는 리스트에 있는 아이들을 불러오면서 student에 넣으란 것
print(students)

# 학생 이름을 길이로 변환
student = ["Iron Man", "Thor",  "I am groot"]
student = [len(i) for i in student] # 리스트 안에 있는 값들을 하나씩 반복하면서 추출한 길이를 출력한다
print(student)

# 학생 이름을 대문자로 변환
student = ["Iron Man", "Thor",  "I am groot"]
student = [i.upper() for i in student]
print(student)