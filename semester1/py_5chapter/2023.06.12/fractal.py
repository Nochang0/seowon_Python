## 
# 이 프로그램은 순환적으로 나무를 그린다.
# 237P

import turtle 

def drawTree(branch, t):
    if branch > 5:
        t.forward(branch)
        t.right(20)
        drawTree(branch-15, t)
        t.left(40)
        drawTree(branch-15, t)
        t.right(20)
        drawTree(branch)
        
def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward()
    t.down()
    t.color("green")
    drawTree(100, t)
    window.exitonclick()
    
main()