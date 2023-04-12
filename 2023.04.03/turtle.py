import turtle; # (1)

# turtle 실습 1
t = turtle.Turtle() # (2)
t.share("turtle") # (3)

t.forward(100) # (4)
t.left(90) # (5)
t.forward(50)

turtle.mainloop() # (6)
turtle.bye()


# turtle 실습 2 (삼각형 만들기)
# t = turtle.Turtle()
# t.share("turtle")

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

turtle.mainloop()
turtle.bye()


# turtle 실습 3
# t = turtle.Turtle()

colors = ["red", "purple", "blue", "green", "yellow", "orange"]

turtle.bdcolor("black")
t.speed(0)
t.wirth(3)
length = 10

while length < 300:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(86)
    length += 5

turtle.mainloop()
turtle.bye()