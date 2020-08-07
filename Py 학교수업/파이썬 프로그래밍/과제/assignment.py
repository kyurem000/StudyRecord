# 현재 인구수
numbers = 312032486

# 사용자로부터 년도를 입력받음
year = int(input("년 수를 입력하세요. : "))

# 사용자로부터 입력받은 년수와 1년의 시간을 곱함
total_year = year * 365 * 24 * 60 * 60

# 인구수 계산 과정1 : 7초마다 1명 출생
people_procreate = total_year // 7

# 인구수 계산 과정2 : 13초마다 1명 사망
people_die = total_year // 13

# 인구수 계산 과정3 : 45초마다 새로운 이민자
people_plus = total_year // 45

# 계산 과정
output = ( numbers + people_procreate + people_plus ) - people_die

# 결과 출력
print("{0}년 후의 인구수는 {1} 입니다.".format(year, output))
