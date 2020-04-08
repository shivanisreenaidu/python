def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def cal():
    num =int(input("1 , 2 , 3 , 4 "))
    print("enter 1.to add 2.to subtract 3.to multiply 4.to divide")
    if(num=='1'):
        add(2,3)
    if(num=='2'):
        sub(2,3)
    if(num=='3'):
        mul(2,3)
    if(num=='4'):
        div(2,3)
