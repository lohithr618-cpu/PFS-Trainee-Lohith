Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a={7,4.5,'python',2+5j,True,False}
print(a)
{False, True, (2+5j), 4.5, 7, 'python'}
type(a)
<class 'set'>
b={2,3,4,9,9,4,0,5}
b
{0, 2, 3, 4, 5, 9}
#set is aunordered
#set is semimutable
#set removes the duplicate values

#add
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}

#subset
a={4,5,5,6,7,8,9}
b={7,8,9}
b.issubset(a)
True
a.issubset(b)
False

#superset
a.issuperset(b)
True
b.issuperset(a)
False

#union
a={1,2,3,4,5,6,7,8}
b={6,7,8,9,10,11,12}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

#intersection
a.intersection(b)
{8, 6, 7}

#update
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10,11,12}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
b
{5, 6, 7, 8, 9, 10, 11, 12}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

#differernce
a={1,2,3,4,5,6,7,8}
b={5,6,7,8,9,10,11,12}
a.difference(b)
{1, 2, 3, 4}
b.difference(a)
{9, 10, 11, 12}

#symmetric difference
a.symmetric_difference(b)
{1, 2, 3, 4, 9, 10, 11, 12}
b.symmetric_difference(a)
{1, 2, 3, 4, 9, 10, 11, 12}

#difference update
a={3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11,12}
a.difference_update(b)
a
{3, 4}
b.difference_update(a)
b
{5, 6, 7, 8, 9, 10, 11, 12}

#inetrsection update
a={2,3,4,5,6,7}
b={1,5,3,4,6,8,9,10}
a.intersection_update(b)
a
{3, 4, 5, 6}
a
{3, 4, 5, 6}
b.intersection_update(a)
b
{3, 4, 5, 6}

#symmetric difference update
a={6,7,8,9,10,11,12}
b={10,11,12,13,14,15}
a.symmetric_difference_update(b)
a
{6, 7, 8, 9, 13, 14, 15}
b.symmetric_difference_update(a)
b
{6, 7, 8, 9, 10, 11, 12}


#pop
a={10,20,30,40,50,60}
a.pop()
50
a={2,3,4,5,6,7}
a.pop()
2

#remove()
a={2,3,4,5,6,7,8,9}
a.remove(7)
a
{2, 3, 4, 5, 6, 8, 9}

#discard
a={4,5,6,7,8,9,10}
a.dicard(8)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.dicard(8)
AttributeError: 'set' object has no attribute 'dicard'. Did you mean: 'discard'?
a.discard(8)
a
{4, 5, 6, 7, 9, 10}

#copy
a.copy()
{4, 5, 6, 7, 9, 10}
b=a.copy()
b
{4, 5, 6, 7, 9, 10}
>>> a
{4, 5, 6, 7, 9, 10}
>>> 
>>> #clear
>>> a.clear()
>>> a
set()
>>> 
>>> #add
>>> a.add(25)
>>> a
{25}
>>> 
>>> #len
>>> a={2,3,4,5,6}
>>> len(a)
5
>>> a.index(3)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.index(3)
AttributeError: 'set' object has no attribute 'index'
>>> a.count(5)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.count(5)
AttributeError: 'set' object has no attribute 'count'
>>> 
>>> #disjoint
>>> a={2,3,4,5,6,7,8}
>>> b={4,5,6,8,9}
>>> a.isdisjoint(b)
False
>>> 
>>> a={2,3,4,5,6,7,8}
>>> b={9,10,11,12,13}
>>> a.isdisjoint(b)
True
