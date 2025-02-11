import turtle
import random

def draw_square(side_length):
    for _ in range(4):  # A square has 4 sides
        turtle.forward(side_length)
        turtle.right(90)  # Turn 90 degrees to form a square corner

# Function to set a random color
def set_random_color():
    r = random.random()  # Random value for red (0-1)
    g = random.random()  # Random value for green (0-1)
    b = random.random()  # Random value for blue (0-1)
    turtle.pencolor(r, g, b)  # Set turtle pen color

# 터틀 초기 설정
turtle.speed(10)
turtle.colormode(1.0)  # Use RGB colors in the range of 0 to 1

# 4개의 정사각형 그리기
for _ in range(4):
    set_random_color()  # Set a random color before drawing
    draw_square(50)  # Draw a square with a side length of 50
    turtle.penup()
    turtle.backward(100)  # Move backward for the next square
    turtle.pendown()

# 창을 닫을 때까지 유지
turtle.done()
