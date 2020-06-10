# 2020-06-10
#  세트

# 집합 (set)
# 중복 안됨, 순서가 없음 
my_set = {1,2,3,3,3}
print(my_set)


java = {"유재석","김태호","양세형"}

python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자를 구하시오)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python도 할 수 있는 개발자를 구하시오)
print(java | python)
print(java.union(python))
# 다시 말하지만 순서는 보장되지 않는다.

# 차집합(java를 할 수 있지만 python을 할 줄 모르는 개발자 )
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊어먹음 
java.remove("김태호")
print(java)
