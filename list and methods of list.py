Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#List[]
a=[5,4.5,"python",6+5j,True]
print(a)
[5, 4.5, 'python', (6+5j), True]
type(a)
<class 'list'>
a=4.5
>>> type(a)
<class 'float'>
>>> b=[4.5]
>>> type(b)
<class 'list'>
>>> 
>>> #methods of list
>>> #append
>>> a=["python","java","c"]
>>> a.append("c++")
>>> a
['python', 'java', 'c', 'c++']
>>> a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["ml","ai"])
>>> a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
>>> 
>>> #extend
>>> a=["ds","ai","ml"]
>>> a.extend(["c","c++"])
>>> a
['ds', 'ai', 'ml', 'c', 'c++']
>>> 
>>> #insert()
>>> a=["black","white"]
>>> a.insert(1,"blue")
>>> a
['black', 'blue', 'white']
>>> 
>>> #index
>>> a=["apple","banana","grapes"]
>>> a.index("grapes")
2
>>> 
>>> #copy
>>> a.copy()
['apple', 'banana', 'grapes']
b=a.copy()
b
['apple', 'banana', 'grapes']

#pop()
a=["hi","hello","how","are","you"]
a.pop()
'you'
a
['hi', 'hello', 'how', 'are']
a.pop("how")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.pop("how")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(2)
'how'
a
['hi', 'hello', 'are']

#remove
a.remove("hello")
a
['hi', 'are']

#sort()
a=["vij","vzg","hyd","chennai"]
a.sort()
a
['chennai', 'hyd', 'vij', 'vzg']
b=[8,2,3,99,35,20,1]
b.sort()
b
[1, 2, 3, 8, 20, 35, 99]
c=[25,0.5,"pyhton",3+8j,True,False]
c.sort()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'str' and 'float'

#reverse
a=["mango","orange","berry"]
a.reverse()
a
['berry', 'orange', 'mango']

#len()
a=["c","c++","java"]
len(a)
3
b="java"
len(b)
4
c=['java']
len(c)
1

#count()
a.count("a")
0
a.count("c")
1

#clear
a=["python","java",".net"]
a.clear()
a
[]
b=[]
b.append("lohith")
b
['lohith']
