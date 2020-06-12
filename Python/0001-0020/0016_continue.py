# 2020-06-10
# continue
# break

# 결석한 학생 
absent = {2, 5} 

# 책을 두고온 학생
no_book = [7]

for student in range(1, 11): # 1 ~ 10
    if student in absent:
        continue # 계속해서 다음 반복을 진행하는 것을 의미
    elif student in no_book:
        print("오늘 수업은 여기까지, {0}은 교무실로 와".format(student))
        break # 지금 상황에서 반복문을 종료하고 끝내는 것을 의미 
    print("{0}, 책 읽어봐".format(student))
