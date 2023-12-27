import turtle as t
t1 = t.Turtle()
t1.shape("turtle")
t1.color("green", "red")
def oneDash():
  t1.forward(5)
  t1.penup()
  t1.forward(5)
  t1.pendown()
for i in range(10):
  t1.pencolor("red")
  oneDash()
  t1.pencolor("blue")
  oneDash()


t1.screen.mainloop()