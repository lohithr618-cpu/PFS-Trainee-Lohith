Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Slicing
>>> a="codegnan"
>>> a[0:3]
'cod'
>>> [0:4]
SyntaxError: invalid syntax
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> a="work until you succeed"
>>> a[:4]
'work'
>>> a[10:14]
' you'
>>> a[5:10]
'until'
>>> a[15:22]
'succeed'
>>> a[15:]
'succeed'
>>> a='vijayawada is a royal city'
>>> a[22:]
'city'
>>> a[16:21]
'royal'
>>> a[:10]
'vijayawada'
>>> a[11:13]
'is'
>>> #Negetive slicing
>>> a='Happy Teachers Day'
>>> a=[-14:]
SyntaxError: invalid syntax
a=[;14]
SyntaxError: invalid syntax
a[:-14]
'Happ'
a[:-13]
'Happy'
a[-4:-1]
' Da'
a[-3:]
'Day'
a[-13:-8]
' Teac'
a[-12:-7]
'Teach'
a='vizag is a city of destiny'
a[:-21]
'vizag'
a[-16:13]
' ci'
a[-15:-11]
'city'
a[-8:]
' destiny'

