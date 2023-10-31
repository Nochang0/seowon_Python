# 202311420 연승현
# 400P 2번

class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"로켓 위치: ({self.x}, {self.y})"

    def moveUp(self):
        self.y += 1



myRocket = Rocket(0, 0)
print("로켓의 높이:", myRocket.y)

myRocket.moveUp()
print("로켓의 높이:", myRocket.y) 
