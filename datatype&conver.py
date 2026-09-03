Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=5
type(a)
<class 'int'>
b=2.5
type(bb)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(bb)
NameError: name 'bb' is not defined. Did you mean: 'b'?
b=2.5
type(b)
<class 'float'>
c='python'
type(c)
<class 'str'>
d="course"
type(d)
<class 'str'>
e='''codegnan'''
type(e)
<class 'str'>
f=2+5j
type(f)
<class 'complex'>
g=2j+5
type(g)
<class 'complex'>
h=5j
type(h)
<class 'complex'>
z=True
type(z)
<class 'bool'>
y=2+3i
SyntaxError: invalid decimal literal
a=j
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a=j
NameError: name 'j' is not defined
#
#
#
#
#datatype conversion
#int
int
<class 'int'>

int(2)
2
int(2.5)
2
int("pythn")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int("pythn")
ValueError: invalid literal for int() with base 10: 'pythn'
int(2+5j)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(2+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(true)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
1
int(False)
0
#
#
#
#float
float(5)
5.0
float(5.25)
5.25
float("python")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float(2+5j)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    float(2+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#
#
#
#str
str(5)
'5'
str(2.5)
'2.5'
str("python)
    
SyntaxError: unterminated string literal (detected at line 1)
str("python")
    
'python'
str(2+5j)
    
'(2+5j)'
str(True)
    
'True'
str(False)
    
'False'
#
    
#
    
#
    
>>> #complex
...     
>>> complex(5)
...     
(5+0j)
>>> complex(2.5)
...     
(2.5+0j)
>>> complex("python")
...     
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
>>> complex(2+5j)
...     
(2+5j)
>>> complex(True)
...     
(1+0j)
>>> complex(False)
...     
0j
>>> #
...     
>>> #
...     
>>> #
...     
>>> #bool
...     
>>> bool(5)
...     
True
>>> bool(2.5)
...     
True
>>> bool("python")
...     
True
bool(2+5j)
    
True
bool(True)
    
True
bool(False)
    
False
