# 193P

import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(200):
    t.forward(2+i/4)
    t.left(30-i/12)

turtle.mainloop0
turtle.bye()