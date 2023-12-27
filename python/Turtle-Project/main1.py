"""Simpler and short version, creating different shapes with different colors"""

import turtle as t

t1 = t.Turtle()
t1.shape("turtle")

# Function to draw a different shapes and fill it with the specified color
def draw_shapes(size, sides, angle, fill_color):
    t1.penup()
    t1.goto(0, 0)
    t1.pendown()
    t1.begin_fill()
    t1.color(fill_color[0], fill_color[1])
    for _ in range(sides):
        t1.forward(size)
        t1.left(angle)
    t1.end_fill()

# Call the functions to draw shapes in reverse order, centered on the screen
draw_shapes(100, 8, 45, ("pink", "blue"))   # Octagon
draw_shapes(100, 7, 51.43, ("orange", "violet"))   # Heptagon
draw_shapes(100, 6, 60, ("yellow", "pink"))   # Hexagon
draw_shapes(100, 5, 72, ("black", "purple"))   # Pentagon
draw_shapes(100, 4, 90, ("yellow", "blue"))   # Square
draw_shapes(100, 3, 120, ("red", "green"))   # Triangle

# Close the turtle graphics window
t.done()
