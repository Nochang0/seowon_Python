# 변수의 자료형 (69P)

print(type(12.30))
# <class 'float'>

print(type("hello"))
# <class 'str'>



# 변수의 참조값 (71P)
x = 3
y = x

print(id(x)) # 140027846628576
print(id(y)) # 140027846628576

y = 10
print(id(y)) # 140027846628800


