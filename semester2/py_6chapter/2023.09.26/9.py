# 301P

# 9

import turtle

aList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

t = turtle.Turtle()

t.speed(2)

for num in aList:
    t.forward(num)
    t.right(90)

turtle.done()
