# 2020-06-09
# 리스트

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨는 몇 번째 칸에 타고 있는가 
print(subway.index("조세호"))

# 하하가 다음 정류장에서 탑승 
subway.append("하하")
print(subway)

# 정형돈을 유재석과 조세호 사이에 탑승
subway.insert(1, "정형돈") # 1번째 자리에 정형돈 탑승
print(subway)

print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능하다
num_list = [ 5, 2, 3, 1, 4 ]
num_list.sort()
print(num_list)

# 순서 뒤집기도 가능하다
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형과 함꼐 사용
numer_list = [999, 2000, 30, 4, 1]
mix_list = [ "조세호", 20, True ]
numer_list.extend(mix_list)
print(numer_list)