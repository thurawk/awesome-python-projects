
import turtle
import random

t = turtle.Turtle()

def random_color():
    colors = ["red", "green","blue", "purple", "black", "pink"]
    return random.choice(colors)

for i in range(5):
    t.color(random_color())
    for i in range(3):
        t.forward(90)
        t.left(120)
    t.penup()
    t.forward(90)
    t.pendown()

t.hideturtle()

turtle.done()