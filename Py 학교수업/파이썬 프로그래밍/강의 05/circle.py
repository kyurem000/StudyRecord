import turtle

turtle.pensize(3) # 펜 두께 3픽셀
turtle.penup() # 펜을 들어올림
turtle.goto(-200, -50)
turtle.pendown() # 펜을 내려 놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작한다.
turtle.color("red")
turtle.setheading(60) # 60도 회전 
turtle.circle(40, steps = 3) # 삼각형을 그린다
turtle.end_fill() # 도형을 색상으로 채운다.


turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill() # 도형 내부를 색상으로 채우기 시작한다.
turtle.color("blue")
turtle.setheading(60) # 45도 회전 
turtle.circle(40, steps = 4) # 사각형을 그린다
turtle.end_fill()

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill() # 도형 내부를 색상으로 채우기 시작한다.
turtle.color("green")
turtle.setheading(35) # 35도 회전 
turtle.circle(40, steps = 5) # 오각형을 그린다
turtle.end_fill()

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill() # 도형 내부를 색상으로 채우기 시작한다.
turtle.color("yellow")
turtle.setheading(30) # 30도 회전 
turtle.circle(40, steps = 6) # 육각형을 그린다
turtle.end_fill()

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill() # 도형 내부를 색상으로 채우기 시작한다.
turtle.color("purple")
turtle.circle(40) # 원을 그린다.
turtle.end_fill()

turtle.color("green")
turtle.penup()
turtle.goto(-130, 50)
turtle.pendown()
turtle.write("화려한 형형색색의 도형", font=("맑은 고딕", 18, "bold"))
turtle.hideturtle()

turtle.done()
