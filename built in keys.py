#built-in functions
#max(),min(),sum(),len(),print(),input(),type(),next(),range()


#fromkeys()
'''a="codegnan"
print(a)

print(list(a))

print(tuple(a))

print(set(a))

#print(dict(a))
b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"lohith")
print(c)

c["g"]="python"
print(c)'''

#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("A value"))
    b=float(input("B value"))
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)
    print(type(a))
    print(type(b))'''


#zip() ->we can combine multiple collection into one collection

'''a=[10,20,30,40,50]
names=["lohith","hemnath","teju","krishna","taju"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

d=set(zip(a,names))
print(d)

e=dict(zip(a,names))
print(e)

f=tuple(zip(a,names))
print(f)'''

#enumerate()->we can give counter to the collection
'''names=["lohith","hemnath","teju","kanthu","taju"]
for i in range(len(names)):
    print(i,names [i])

b=list(enumerate(names))
print(b)

c=tuple(enumerate(names))
print(c)

d=set(enumerate(names))
print(d)

e=dict(enumerate(names))
print(e)'''

#annonymous function ->annonymous functions are nameless functions and we use a keyword called as lambda to create annonymous functions

'''def fun(x):
    print(2*x+5)
fun(5)'''

'''def f():
    x=int(input("value"))
    print(2*x+5)
f()'''

#syntax
#a=lambda arg:exp

'''a=lambda x:2*x+5
print(a(5))


b=int(input("enter value"))
c=lambda x:2*x+5
print(c(b))'''

'''a=int(input("enter a value"))
b=int(input("enter b value"))
c=lambda x,y:2*a+b
print(c(a,b))'''

'''a=lambda x,y:x*y
print(a(4,5))'''

'''a="python"
#PYTHON
b=lambda a:a.upper()
print(b(a))'''

'''b=lambda a:a.upper()
print(b("python"))'''

'''fname="lohith"
lname="reddy"
a=lambda x:x
print(a(fname+" "+lname))'''

'''a,b=[x for x in input("names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter()
#a=[2,6,7,9,10,12,15,20,40,55,60,80]
'''if a%2==0:
    print(a)#error'''

'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda a:a%2==0,a))
print(b)'''

#[],(),{},set()
'''a=[]
print(type(a))

b=()
print(type(b))

c=set()
print(type(c))

d={}
print(type(d))

a=[[],(),set(),{}," ",None,3,6.7,"python",6+5j,True,False]
b=list(filter(None,a))
print(b)'''


#map()->each object from a collection and forms a new collection

'''a=[2,4,6,8,9,10,12,15,20,25]
b=[1,5,3,0,4,20,25,30,60,80]
c=list(map(max,a,b))
print(c)

d=list(map(min,a,b))
print(d)'''

#run_time input()
'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=[int(x) for x in input("values").split(",")]
print(a+b)'''

'''a,b=int(input("enter the values").split(","))
print(a+b)#error'''

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("data").split(",")
print(a+b)'''

'''a,b=[x for x in input("data").split(",")]
print(a+b)'''

'''a,b=map(str,input("data").split(","))
print(a+b)'''

'''a=list(map(int,input("data").split(",")))
print(a)'''

'''a=tuple(map(int,input("data").split(",")))
print(a)'''

'''a=set(map(int,input("data").split(",")))
print(a)'''

'''a=list(map(str,input("data").split(",")))
print(a)'''

'''a=list(map(eval,input("data").split(",")))
print(a)'''

a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)
