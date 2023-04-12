# 변수 선언하기 (67P)

import turtle;

t = turtle.Turtle()
t.share("turtle")

radius = 50

t.circle(radius) # 반지름이 50인 원이 그려진다.
t.fd(30)
t.circle(radius) # 반지름이 50인 원이 그려진다.
t.fd(30)
t.circle(radius) # 반지름이 50인 원이 그려진다.

turtle.mainloop()
turtle.bye()