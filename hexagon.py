import turtle
import random

def draw_hexagon(size):
    """Draw a hexagon with the given size."""
    for _ in range(6):  # A hexagon has 6 sides
        turtle.forward(size)
        turtle.right(60)  # Each exterior angle of a hexagon is 60 degrees

# Function to set a random color
def set_random_color():
    r = random.random()  # Random value for red (0-1)
    g = random.random()  # Random value for green (0-1)
    b = random.random()  # Random value for blue (0-1)
    turtle.pencolor(r, g, b)  # Set turtle pen color

# Turtle setup
turtle.speed(10)
turtle.colormode(1.0)  # Use RGB colors in the range of 0 to 1

# Draw multiple hexagons
for _ in range(10):  # Draw 10 hexagons
    set_random_color()
    size = random.randint(30, 100)  # Random size for the hexagon
    turtle.penup()
    turtle.goto(random.randint(-200, 200), random.randint(-200, 200))  # Random position
    turtle.pendown()
    draw_hexagon(size)

# Keep the window open
turtle.done()
