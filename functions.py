#functions

'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#//,**,%
'''def calculate(a,b):
    print("the int devision is",a//b)
    print("the power is",a**b)
    print("the modulous div is",a%b)
calculate(1,2)
calculate(10,20)
calculate(7,8)'''

'''def add(a,b):
    c=a+b
    print(c)
add(4,5)'''

'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''

'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()
add()'''


'''def fullname():
    fname=input("fname")
    lname=input("lname")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(3,4)'''


'''def mul(a,b):
    return a*b
print(mul(5,2))'''

#Print v/s return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal (2,4)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(5,4))'''

'''def cal():
    a=int(input("a value:"))
    b=int(input("b value:"))
    option=int(input("Enter the option: \n1.add \n2.sub \n3.mul"))
    if option==1:
        print("the sum is:",a+b)
    elif option==2:
        print("the sub is:",a-b)
    elif option==3:
        print("the mul is:",a*b)
cal()'''

def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input("choose the value \n1add \n2.sub \n3.mul"))  
    if option==1:
               add()
    elif option==2:
                sub()
    elif option==3:
                mul()
        
    



    
    


