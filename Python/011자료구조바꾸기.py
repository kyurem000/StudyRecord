# 2020-06-10
# 자료구조의 변경 

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))
# 타입이 리스트

menu = tuple(menu)
print(menu, type(menu))
# 타입이 튜플 

menu = set(menu)
print(menu, type(menu))
# 타입이 세트 