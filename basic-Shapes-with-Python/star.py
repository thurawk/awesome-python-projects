import turtle
import random

def draw_star(size):
    """Draw a star with the given size."""
    for _ in range(5):  # A star has 5 points
        turtle.forward(size)
        turtle.right(144)  # Angle to form a star

# Function to set a random color
def set_random_color():
    r = random.random()  # Random value for red (0-1)
    g = random.random()  # Random value for green (0-1)
    b = random.random()  # Random value for blue (0-1)
    turtle.pencolor(r, g, b)  # Set turtle pen color

# Turtle setup
turtle.speed(10)
turtle.colormode(1.0)  # Use RGB colors in the range of 0 to 1

# Draw multiple stars
for _ in range(10):  # Draw 10 stars
    set_random_color()
    size = random.randint(30, 100)  # Random size for the star
    turtle.penup()
    turtle.goto(random.randint(-200, 200), random.randint(-200, 200))  # Random position
    turtle.pendown()
    draw_star(size)

# Keep the window open
turtle.done()
