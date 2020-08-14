def add_txt(t1, t2='파이썬'):
    print(t1+':'+t2)

add_txt('베스트') # '베스트:파이썬'이 출력 
add_txt(t2='파이썬은', t1='입문용 최고') # '입문용 최고:파이썬은'이 출력 

def func1(*args):
    print(args)

def func2(width, height, **kwargs):
    print(kwargs)

func1() # 빈 튜플() 출력 
func1(3,5,1,5) # (3,5,1,5) 출력

fucn2(10,20) # 빈 사전 {}이 출력 
fucn2(10,20,depth=50,color='blue') # {depth=50, color='blue'}이 출력 
