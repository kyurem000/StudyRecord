# 2020-06-10
# for (반복문)

for waiting_no in [10, 20, 30, 40, 50]:
    print("대기번호 : {0} ".format(waiting_no))


for waiting_no2 in range(1, 6):
    print("대기번호 : {0} ".format(waiting_no2))


star = ["아이언맨", "토르", "그루트"]
for customer in star:
    print("{0}, 커피가 준비되었습니다.".format(customer))