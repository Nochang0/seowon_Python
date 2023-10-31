# 202311420 연승현
# 401P 4번

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f"사각형 좌표: ({self.x}, {self.y}), 크기: {self.width}x{self.height}"

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def getArea(self):
        return self.width * self.height

    def overlap(self, r):
        if (self.x < r.getX() + r.width and
                r.getX() < self.x + self.width and
                self.y < r.getY() + r.height and
                r.getY() < self.y + self.height):
            return True
        else:
            return False

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(10, 10, 100, 100)
result = r1.overlap(r2)

if result == True:
    print("r1과 r2는 서로 겹칩니다.")
else:
    print("r1과 r2는 서로 겹치지 않습니다.")
