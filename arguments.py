#split bill()
'''def splitbill():
    a=int(input("enter the total number:"))
    b=int(input("enter the total amount:"))
    print(b//a)
splitbill()'''



'''def splitbill():
    a=int(input("enter the total number:"))
    b=int(input("enter the total amount:"))
    print("perhead bill is {}".format(b//a))
    print(f"perhead bill is {b//a}")
splitbill()'''


'''def splitbill():
    a=int(input("enter the total number:"))
    b=int(input("enter the total amount:"))
    c=(b//a)
    print("perhead bill is {}".format(c))
    print(f"perhead bill is{c}")
splitbill()'''

#keywords and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="lohith"
    mailid="lr@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=10,name="lohith",mailid="lr@gmail.com")
Details(10,"lohith","lr@gmail.com")
Details("lohith","lr@gmail.com",10)'''

#employee->name,salary,designation
'''def Details(name,salary,designation):
    print(name,salary,designation)
Details(name="name",salary="salary",designation="designation")
Details("lohtih",25000,"employee")
Details(name="lohith",salary=25000,designation="employee")'''

#default arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("rice",1800)'''

'''def grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''def grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dhal")'''

'''def grocery(item="ghee",price):
    #non-def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(500)'''

#bakery->cake,price,qty
'''def bakery(cake,price,qty):
    print("item is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
bakery("choclate",500,3)'''

'''def bakery(cake="venila",price=350,qty=3):
    print("item is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
bakery()'''

'''def bakery(item="red velvet",price,qty):
    #non-def arg follows def arg
    print("item is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
bakery(850,5)'''

'''def bakery(cake,price=850,qty=5):
    print("item is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
bakery("red velvot")'''

#* arguments-> * is used to unpack the elements

'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)'''

'''a=(2,3,4,5,6,7,8,9)
print(a)
print(*a)'''

'''a={2,3,4,5,6,7,8,9}
print(a)
print(*a)'''

'''a={"name":"lohith","year":2026}
print(a)
print(*a)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8
print(a)
print(b)
print(c)'''#error

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,*b,c=1,2,3,4,5,6,7,8,9
print(a)
print(*b)
print(c)'''

'''a,*b,*c=1,2,3,4,5,6,7,8,9
print(a)
print(*b)
print(*c)'''#error

'''a,b,c="codegnan"
print(a)
print(b)
prine(c)'''#error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''

#variable length arguments
        #def-variable lenght arguments automatically stores in tuple and we use * arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
b=[4,5,6,7,8,9]
check(*b)
c=(3,4,5,6)
check(*c)
d={6,7,8,9,1}
check(*d)
e={"year":2026,"month":"sep"}
check(*e)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,6,7)
check1(2,3,4.5,7,3.8)
check1(3,4,5,7,8.9,2.5,3.5,"lohith",5+9j,True,False)'''

#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"names":["kanthu","hemanth","teja"],
    "marks":[150,250,200],"status":["a","P","P"]}
details(**d)'''

#both * and **
'''def final(*a,**b):
    d=2
    print(a)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is ",j)
final()
data=(2,3,4,5,6,5.5)
final(*data)
details={"names":["kanthu","teja","hemanth"],"marks":[20,25,30]}
final(**details)
final(*data,**details)'''

#patterns
#right angle triangle



    
    




