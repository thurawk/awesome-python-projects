import turtle
import random

def draw_pentagon(size):
    """Draw a pentagon with the given size."""
    for _ in range(5):  # A pentagon has 5 sides
        turtle.forward(size)
        turtle.right(72)  # Each interior angle of a pentagon is 72 degrees

# Function to set a random color
def set_random_color():
    r = random.random()  # Random value for red (0-1)
    g = random.random()  # Random value for green (0-1)
    b = random.random()  # Random value for blue (0-1)
    turtle.pencolor(r, g, b)  # Set turtle pen color

# Turtle setup
turtle.speed(10)
turtle.colormode(1.0)  # Use RGB colors in the range of 0 to 1

# Draw multiple pentagons
for _ in range(10):  # Draw 10 pentagons
    set_random_color()
    size = random.randint(30, 100)  # Random size for the pentagon
    turtle.penup()
    turtle.goto(random.randint(-200, 200), random.randint(-200, 200))  # Random position
    turtle.pendown()
    draw_pentagon(size)

# Keep the window open
turtle.done()
