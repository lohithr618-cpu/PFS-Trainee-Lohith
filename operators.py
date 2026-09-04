Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
##arthimatic
a=5
b=3
print(a+b)
8
print(a-b)
2
print(a*b)
15
print(a//b)
1
print(a/b)
1.6666666666666667
print(a%b)
2
print(a**b)
125

#assignment
a=6
b=3
a+=b
a
9
a-=3
a
6
a*=2
a
12
a/=3
a
4.0
a//=2
a
2.0
a%=2
a
0.0
a**=4
a
0.0
b
3
b+=3
b
6
b-=2
b
4
b*=2
b
8
b/=2
b
4.0
b//=2
b
2.0
b**=3
b
8.0
b%=2
b
0.0
b**=2
b
0.0
a+b
0.0

#comparision
a=8
b=4
a<b
False
a>b
True
a<=b
False
a>=b
True
a!=b
True
a==b
False

#comparision
a=8
b=3
a<b and b>a
False
a>b and b<a
True
a<=b and b>=a
False
a!=b and a==b
False
a<b or a>b
True
a>b or a<b
True
a<=b
False
a<=b or a>=b
True
a!=b or a==b
True
not True
False
not False
True
a<b and b>a
False

#identify
a=3
type(a) is int
True
typr(a) is not int
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    typr(a) is not int
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(a) is not int
False
b=3.5
type(b) is float
True
type(b)
<class 'float'>
type(b) is not float
False
c="string"
typr(c) is not str
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    typr(c) is not str
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(c) is not str
False

#memebership
>>> a=1,2,3,4,5,6,7
>>> 9 in a
False
>>> 5 in a
True
>>> 0 not in a
True
>>> 
>>> #bitwiseNameError: name 'typr' is not defined. Did you mean: 'type'?
>>> #bitwiseNameError: name 'typr' is not defined. Did you mean: 'type'?
>>> #bitwise
>>> a=3
>>> b=2
>>> bin(a)
'0b11'
>>> bin(b)
'0b10'
>>> a&b
2
>>> a|b
3
>>> a=3
>>> ~a
-4
>>> b=-3
>>> ~b
2
>>> -(b+1)
2
>>> a=3
>>> b=2
>>> a^b
1
>>> a=3
>>> a<<2
12
>>> a=3
>>> a>>2
0
