# 301P

# 11

import turtle
import random

die = [1, 2, 3, 4, 5, 6]

one = turtle.Turtle()
one.color("blue")
one.shape("arrow")

two = turtle.Turtle()
two.color("red")
two.shape("turtle")

one.penup()
one.goto(-200, 20)
one.pendown()

two.penup()
two.goto(-200, -20)
two.pendown()

while one.xcor() < 200 and two.xcor() < 200:
    
    distance_one = random.choice(die) * 10
    one.forward(distance_one)
    
    distance_two = random.choice(die) * 10
    two.forward(distance_two)

if one.xcor() >= 200 and two.xcor() >= 200:
    print("무승부!")
elif one.xcor() >= 200:
    print("파란색 터틀 승리!")
else:
    print("빨간색 터틀 승리!")

turtle.done()
