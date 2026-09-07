Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#replace
a="wait until u succeed"
a.replace("wait","work")
'work until u succeed'
#upper()
a="python"
a.upper()
'PYTHON'
b="lohith"
b.upper()
'LOHITH'

#lower()
a="CODE"
a.lower()
'code'
b="JAVA"
b.lower()
'java'

#capitalize()
a="code python"
a.capitalize()
'Code python'

#title()
b=" i am lohith"
b.title()
' I Am Lohith'
c="python full stack"
c.title()
'Python Full Stack'

#startswith
a="hellow world"
a.startswith()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.startswith()
TypeError: startswith expected at least 1 argument, got 0
a.startswith("h")
True

#endswith
a="hellow world"
a.endswith("d")
SyntaxError: multiple statements found while compiling a single statement
b="python course"
b.endswith("e")
True
#isalpha
a.isalpha()
False
b="name"
b.isalpha()
True

#isdigit
c="1234"
c.isdigit()
True

#isalnum()
a="lohith123"
a.isalnum()
True

#strip
#lstrip,rstrip
a="       lohith"
a.lstrip()
'lohith'
b="reddy     "
b.rstrip()
'reddy'


#concatination
a="lohith"
b="reddy"
print(a+b)
lohithreddy

fname="lohith"
lname="reddy"
print(fnamw+lname)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(fnamw+lname)
NameError: name 'fnamw' is not defined. Did you mean: 'fname'?
print(fname+lname)
lohithreddy
print(fname+" "+lname)
lohith reddy
print(fname.title()+" "+lname.title())
Lohith Reddy
print((fname+" "+lname).titile())
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print((fname+" "+lname).titile())
AttributeError: 'str' object has no attribute 'titile'. Did you mean: 'title'?
print((fname+" "+lname).title())
Lohith Reddy

#split()
a=" python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']

#join
a="vij","hyd","vzg"
"".join(a)
'vijhydvzg'
" ".join(a)
'vij hyd vzg'
"k".join(a)
'vijkhydkvzg'
b="hello"
"m".join(b)
'hmemlmlmo'

#formatting
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
print("the sum is,a+b")
the sum is,a+b
city="vij"
print("city is",city)
city is vij

#formatmethod
a="motu"
b="pathulu"
print("hello {}{}".format(a,b))
hello motupathulu
print("hello {} {}".format(a,b))
hello motu pathulu
print("hello {} hello {}".format(a,b))
hello motu hello pathulu

#fstring()
a="pawan"
>>> b="kalyan"
>>> print(f"hello {a}{b}")
hello pawankalyan
>>> print(f"hello {a} {b}")
hello pawan kalyan
>>> print(f"hello {a} hello {b}")
hello pawan hello kalyan
>>> hello pawan hello kalyan
SyntaxError: invalid syntax
>>> 
>>> 
>>> #tasks
>>> #formatmethod
>>> a="lohith'
SyntaxError: unterminated string literal (detected at line 1)
>>> a="lohith"
>>> b="reddy"
>>> print("firstname {} lastname {}".format(a,b))
firstname lohith lastname reddy
>>> 
>>> #fstring
>>> a="lohith'
SyntaxError: unterminated string literal (detected at line 1)
>>> a='lohith'
>>> b='reddy'
>>> print(f"firstname {a} lastname {b}")
firstname lohith lastname reddy
>>> 
>>> a=2
>>> b=3
>>> c=a+b
>>> print("the sum is {}".format(c))
the sum is 5
>>> print("the sum is {c}")
the sum is {c}
>>> print(f"the sum  is {a+b}")
the sum  is 5
>>> print("the sum is {}".format(a+b))
the sum is 5
