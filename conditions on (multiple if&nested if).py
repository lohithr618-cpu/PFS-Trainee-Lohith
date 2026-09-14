#conditions
#if-elif-else  coinditions by using comparition operators
'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=5
b=6
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=9
b=12
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")'''

'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not true")
else:
    print("true")'''
#logical omperators

'''a=8
b=5
if a<b and b>a:
    print("true")
elif a>b or a<b:
    print("yes")
elif not a!=b or a==b:
    print("logical")
else:
    print("failed")'''

#identify opearators[is,is not]
'''a=10
b=20
if type(a) is float:
    print("true")
elif type(b) is not float:
    print("yes")
else:
    print("fail")'''

#membership operators[in,not in]
'''a=[1,2,3,4,5,6,7,8,9]
if 10 in a:
    print("yes")
elif 10 not in a:
    print("true")
else:
    print("failed")'''


#multiple-if
#comparision opearators
'''a=5
b=10
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=5
b=10
if a<b:
    print("less")
elif b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=5
b=10
if a==b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''
#logical operators[and,or,not]
'''a=5
b=10
if a<b and a>b:
    print("less")
if b>a or a<b:
    print("greater")
if not a!=b or a==b:
    print("not equal")'''

#identify oprators[is,is not]
'''a=5
b=10
if type(a) is float:
    print("true")
if type(b) is int:
    print("yes")
if type(a) is not float:
    print("graet")'''

#membership operators
'''a=[1,2,3,4,5,6,7,8,9]
if 3 in a:
    print("yes")
if 7 in a:
    print("greater")
if 10 not in a:
    print("true")'''

#neated-if
'''a=6
b=12
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=6
b=12
if a>b:
    print("less")
if b>a:
    print("greater")'''

'''a=6
b=12
if a==b:
    print("less")
    if b>a:
        print("greater")'''

'''a=10
b=20
if a<b:
    print("less")
    if a==b:
        print("equal")'''

'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("true")'''

'''a=30
b=50
if a>b:
    print("less")
    if b>a:
        print("equal")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b>a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a>b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("true")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b==a:
        print("equal")
    elif a!=b:
        print("not equal")
    else:
        print("false")
else:
    print("true")'''

#nested-if on logical operators[and,or,not]
'''a=20
b=30
if a<b and b>a:
    print("true")
    if a<=b or a>=b:
        print("greater")
        if not a!=b or a==b:
            print("yes")
else:
    print("failed")'''

#nested-if on identify operators
'''a=20
b=10
if type(a) is int:
    print("int")
    if type(b)is not float:
        print("not float")
    elif type(a)is not str:
            print("not str")
else:
    print("failed")'''

#nested-if on membeship operators
a=[1,2,3,4,5,6,7,8,9,10]
if 2 in a:
    print("yes")
    if 4 in a:
        print("true")
        if 11 not in a:
            print("not in a")
else:
    print("failed")
    









