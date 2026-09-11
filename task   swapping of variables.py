#swaping of 2 variables

#by using with out temp veriable
'''a=20
b=10
a,b=b,a
print("value of a is",a)
print("value of b is",b)'''

#by using temp variable

'''a=20
b=10
temp=a
a=b
b=temp
print("value of a is",a)
print("value of b is",b)'''

#by using arthimetic operators

'''a=20
b=10
a=a+b
b=a-b
a=a-b
print("value of a is",a)
print("value of b is",b)'''


#by using number format

'''a=20
b=10
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d"%(a,b))'''

#swaping of two strings
#by two variables
'''a="python"
b="java"
a,b=b,a
print("str of a is",a)
print("str of b is",b)'''


#by using temp

'''a="python"
b="java"
temp=a
a=b
b=temp
print("str of a is",a)
print("str of b is",b)'''

#by using number format

a="python"
b="java"
a,b=b,a
print("swapping of two variables are a=%s,b=%s"%(a,b))




