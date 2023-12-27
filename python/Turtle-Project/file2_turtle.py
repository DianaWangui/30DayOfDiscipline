import turtle as t
t1 = t.Turtle()
t2 = t.Turtle()

t1.shape("turtle")
t1.color("green", "red")
t1.begin_fill()
t1.circle(100)
t1.end_fill()

t1.penup()
t1.rt(90)
t1.forward(100)
t1.pendown()
t1.begin_fill()
t1.hideturtle()
t1.circle(40)
t1.end_fill()
t1.goto(-100, 100)
t1.showturtle()
print(t1.pos())


t1.screen.mainloop()