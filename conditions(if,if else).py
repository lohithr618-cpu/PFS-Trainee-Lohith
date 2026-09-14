#conditions

#if-condition by using comparision operators
#<,>,<=,>=,!=,==

'''a=10
b=20
if a<b:
    print("true")'''

'''a=10
b=20
if a>b:
    print("less")'''

'''a=5
b=12
if a<=b:
    print("true")'''

'''a=9
b=5
if a>=b:
    print("greater")'''

'''a=10
b=20
if a!=b:
    print("true")'''


'''a=10
b=10
if a==b:
    print("same")'''

'''a="python"
if a=="python":
    print("yes")'''

'''a="java"
b="python"
if a!=b:
    print("true")'''

'''a="java"
if a!="python":
    print("false")'''

'''a=int(input("enter a value"))
b=int(input("enter b value"))
if a>b:
    print("yes")'''

'''a=int(input("a value"))
if a>30:
    print("true")'''

#if-condition using logical operators
#and,or,not
'''a=4
b=8
if a<b and b>a:
    print("less")'''

'''a=9
b=8
if a<=b and b>=a:
    print("less")'''

'''a=4
b=8
if a!=b and b==a:
    print("less")'''


'''a=4
b=8
if a<b or b>a:
    print("less")'''

'''a=4
b=8
if a<=b or b>=a:
    print("less")'''

'''a=4
b=8
if a!=b or b==a:
    print("less")'''

'''a=4
b=8
if not a<b and b>a:
    print("less")'''

'''a=4
b=8
if not a<=b or b>=a:
    print("less")'''

'''a=4
b=8
if not a!=b and b==a:
    print("less")'''

'''a=int(input("enter a value"))
b=int(input("enter b value"))
if a<b or a>b:
    print("true")'''

#if-condition by using identify operators
#is,is not
'''a=10
if type(a) is int:
    print("it is int")'''

'''a=7
if type(a) is not int:
    print("is not int")'''

'''a=10.5
if type(a) is not int:
    print("its not int")'''

'''a=int(input("enter a value"))
if type(a) is int:
    print("it is int")'''

#if-condition by using membership operators
#in,in not
'''a=[2,3,4,5,6,7,8,9]
if 5 in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 10 not in a:
    print("true")'''

'''a=int(input("enter a value"))
if 30  in a:
    print("true")'''#error

'''a=[2,3,4,5,6,7,8,9]
b=int(input("enter the value"))
if b in a:
    print("true")'''



#if-else conditions by using comparision operators
#<,>,<=,>=
'''a=5
b=9
if a<b:
    print("less")
else:
    print("false")'''

'''a=5
b=9
if a>b:
    print("less")
else:
    print("false")'''

'''a=5
b=9
if a!=b:
    print("less")
else:
    print("false")'''

'''a=5
b=9
if a==b:
    print("less")
else:
    print("false")'''

#logical oprators
#and,or,not
'''a=5
b=3
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=3
b=8
if a<b or b>a:
    print("true")
else:
    print("false")'''

'''a=5
b=8
if not a>b and b<a:
    print("true")
else:
    print("false")'''

#identity operators
#is,is not
'''a=5
if type(a) is int:
    print("true")
else:
    print("false")'''

'''a=5
if type(a) is float:
    print("true")
else:
    print("false")'''

'''a=10.5
if type(a)is not int:
    print("true")
else:
    print("false")'''

#membership operators
#in,not in
'''a=[1,2,3,4,5,6,7,8,9]
if 2 in a:
    print("yes")
else:
    print("no")'''

'''a=[1,2,3,4,5,6,7,8,9]
if 2 not in a:
    print("yes")
else:
    print("no")'''

a=[1,2,3,4,5,6,7,8,9]
b=int(input("enter the value"))
if b in a:
    print("yes")
else:
    print("no")



