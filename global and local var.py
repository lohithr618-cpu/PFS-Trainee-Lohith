#global and local variables
#first case of global varaibles
'''a=4
def check():
    print("inside value is",a)
check()
print("outside  value is",a)'''

#second case of global variables
'''a=5
def check1():
    a=10
    a=a**2
    print("inside value is",a)
check1()
print("outside value is",a)'''

#third case of global variable
'''a=3
b=5
def check2():
    a=8
    print("inside value is",a)
    a=10
    print("inside value is ",a+5)
    b=10#local
    print("inside value is ",a+b)
check2()
print("outside value is",a)
print("outside value is",b)'''


#usage of global keyword
'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=7
    print("updated value is",a)
    #global b
    b=13
    b=b+a
    print("b value is",b)
final()
print("a value is",a)
print("b value is ",b)'''

#CHR,ORD
#ASCII
'''print(chr(65))
print(chr(90))
print(chr(92))


print(ord("a"))
print(ord("z"))
#print(ord(98))
#print(chr("z"))'''

#task
'''for i in range(65,91):
    print(chr(i),end=" ")

for i in range(97,123):
    print(chr(i),end=" ")'''


'''a=input("enter the name:")
for i in a:
    print(i,":",ord(i))'''

#railway ticket
ticket_price=1000
def gender():
    a=input("enter the gender : ")
    if a=="male":
        age=int(input("enter the age:"))
        if age<60:
            print("the amount is :",ticket_price)
        elif age>60:
            print("the amount is :",(ticket_price-(30/100)*ticket_price))
    elif a=="female":
        age=int(input("enter the age:"))
        if age<60:
            print("the amount is:",(ticket_price-(30/100)*ticket_price))
        elif age>60:
            print("the amount is:",(ticket_price-(50/100)*ticket_price))
gender()
