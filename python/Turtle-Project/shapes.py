"""This was my first try but found I was repeating myself
so I implemented one thats is simple.
in the file main.py"""

import turtle as t
t1 = t.Turtle()
t1.shape("turtle")

#Create a triangle and fill with green color
def triangle(size, angle):
  t1.begin_fill()
  t1.color("red", "green")
  for i in range(3):
    t1.forward(size)
    t1.left(angle)
  t1.end_fill()


#Create a square and fill only the remaining part without the reiangle with blue color
def square(size, angle):
  t1.begin_fill()
  t1.color("yellow", "blue")
  for i in range(4):
    t1.forward(size)
    t1.left(angle)
  t1.end_fill()
  

#Create a pentagon and fill only the reamining part with no square part with purple
def pentagon(size, angle):
  t1.begin_fill()
  t1.color("black", "purple")
  for i in range(5):
    t1.forward(size)
    t1.left(angle)
  t1.end_fill()

def hexagon(size, angle):
  t1.begin_fill()
  t1.color("yellow", "pink")
  for i in range(6):
    t1.forward(size)
    t1.left(angle)
  t1.end_fill()

def heptagon(size, angle):
  t1.begin_fill()
  t1.color("orange", "violet")
  for i in range(7):
    t1.forward(size)
    t1.left(angle)
  t1.end_fill()

def octagon(size, angle):
  t1.begin_fill()
  t1.color("pink", "blue")
  for i in range(8):
    t1.forward(size)
    t1.left(angle)
  t1.end_fill()



# Call the function to draw a square with side length of 50 and an angle of 60 degrees
octagon(100, 45)
heptagon(100, 51.5)
hexagon(100, 60)
pentagon(100, 72)
square(100, 90)
triangle(100,120)  


t1.screen.mainloop()









