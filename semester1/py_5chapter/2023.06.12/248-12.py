# 202311420 연승현
# 248P 12번

def getSorted(x, y):
    if x > y:
        return y, x
    else:
        return x, y

num1 = int(input("첫 번째 정수: "))
num2 = int(input("두 번째 정수: "))

result = getSorted(num1, num2)
print(result)