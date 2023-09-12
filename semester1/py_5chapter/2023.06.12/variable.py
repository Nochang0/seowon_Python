# 238P ~ 239P

# local
def myfunc():
    x = 100
    print(x)
    
myfunc()


# global
gx = 100

def myfunc():
    print(gx)
    
myfunc()
print(gx)


# local 2
def myfunc():
    x = 100
    print(x)

def main():
    x = 100
    print(x)
    
myfunc()
main()


# global (but local)
gx = 100

def myfunc():
    gx = 200
    print(gx)
    
myfunc()
print(gx)


# global 2
gx = 100

def myfunc():
    global gx
    gx = 200
    print(gx)
    
myfunc()
print(gx)
