
import turtle

def draw_circle(radius):
    turtle.circle(radius)

# 터틀 초기 설정
turtle.speed(10)

# 6개의 원 그리기
for _ in range(4):
    draw_circle(50)  # 반지름이 50인 원 그리기
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    #turtle.penup()
    #turtle.forward(100)  # 다음 원을 그리기 위해 이동
    #turtle.pendown() 

# 창을 닫을 때까지 유지
turtle.done()