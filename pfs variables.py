Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(5+9)
14
a=10
b=10
print(a+b)
20
d=50
>>> print(d)
50
>>> e=100
>>> print(E)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(E)
NameError: name 'E' is not defined. Did you mean: 'e'?
>>> print(e)
100
>>> 1a=10
SyntaxError: invalid decimal literal
>>> a1=10
>>> print(a1)
10
>>> if=10
SyntaxError: invalid syntax
>>> del=10
SyntaxError: invalid syntax
>>> name@=10
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name@=10
NameError: name 'name' is not defined
>>> name_=10
>>> print(name_)
10
>>> age=50
>>> print(Age)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(Age)
NameError: name 'Age' is not defined. Did you mean: 'age'?
>>> print(age)
50
>>> a=10,b=10
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=10;b=20
>>> print(a+b)
30
a='lohith"
SyntaxError: unterminated string literal (detected at line 1)
a="lohith"
b="reddy"
print(a+b)
lohithreddy
a="lohith";b="reddy"
print(a+b)
lohithreddy
a,b="lohtih","reddy"
print(a+" "+b)
lohtih reddy
print(a+_+b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(a+_+b)
NameError: name '_' is not defined
a,b="lohtih","reddy"
print(a+_+b)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(a+_+b)
NameError: name '_' is not defined
a,b="reddy","lohith"
print(a,b)
reddy lohith
a,b,c=(10,20,30)
print(a,b,c)
10 20 30
