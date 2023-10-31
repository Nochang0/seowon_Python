# 202311420 연승현
# 401P 3번

class Box:
    def __init__(self, l, h, d):
        self.l = l
        self.h = h
        self.d = d
        
    def __str__(self):
        return f"{self.l} {self.h} {self.d}"
    
    def setLength(self, l, h, d):
        self.l = l
        self.h = h
        self.d = d
        
    def getHeight(self):
        return self.h
    
    def getLength(self):
        return self.l
    
    def getDepth(self):
        return self.d
        
        
b1 = Box(100, 100, 100)
print(b1)
print(f"상자의 부피는 {b1.getHeight()*b1.getLength()*b1.getDepth()}")
