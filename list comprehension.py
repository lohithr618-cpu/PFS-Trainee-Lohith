#list conprehension
'''a=["python","java","dsa"]'''
#["PYTHON","JAVA","DSA"]

#print(a.upper())
#it will shows error ,list dont have upper

'''for i in a:
    print(i.upper(),end=" ")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#syntax for list comprehension
#a=[expr for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

#tasks

'''b=["apple","mango"]
#b=["Apple","Mango"]
c=[i.capitalize() for i in b]
print(c)'''

'''c=[1,2,3,5,6,8,12,13]
#c=[1,4,9,16,25,36,84,144,169]
d=[pow(i,2) for i in c]
d=[i**2 for i in c]
d=[i*i for i in c]
print(d)'''

'''a=[i for i in range(0,21)]
print(a)'''

#if-usage in list comprehension
'''c=[i for i in range(16)if i%2==0]
print(c)'''

'''a=[i*i for i in range(31) if i%2==0]
print(a)'''


'''b=["grapes","berry","mango","kiwi","dragon","apple"]
c=[i for i in b if "a" in i]
print(c)'''


'''b=["grapes","berry","mango","kiwi","dragon","apple"]
c=[i for i in b if "a" not in i]
print(c)'''

#no-elif usage in list comprehension

#if-else usage in list comprehension

'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
c=[a[i]+b[i] for i in range(len(a))]
c=[a[i]+b[i] for i in range(5)]
print(c)

