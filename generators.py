#genarators
  #def->no tuple comprehension in above cases if we remove those braces and keep parantaces then outcome is generated

#a=[expr for var in collection/range]

'''a=[i for i in range(16)]
print(a)
print(type(a))'''#type list

'''a=(i for i in range(16))
print(a)
print(*a)
print(type(a))'''#type generator

'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
#print(set(a))'''

#main def-generators
#a generator is also a function which can be use as an iterator(loop) by producing group of values.wheir we can use yield keyword


#return vs yield
#return is terminate the function where as yield can pass the function and go on with every successive iteration


'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))'''

#yield v/s return
'''def mygen():
    #return "python"
    #return "java"
    #return "c"
    return "python","java","c"
print(*mygen())'''

'''def mygen():
    yield "vij"
    yield "hyd"
    yield "vzg"
print(*mygen())
#next
b=mygen()
print(next(b))
print(next(b))
print(next(b))'''

#built-in functions
#max(),min(),sum(),len(),print(),input(),type(),next(),range()

a=(1,2,3,4,5,6)
print(max(a))
print(min(a))
print(sum(a))
print(len(a))
print(type(a))
def d(c):
    for i in range (c):
        yield c
        c=c+2
        yield c
        c=c+2
        yield c
print(*d(c))
print(next(d))



