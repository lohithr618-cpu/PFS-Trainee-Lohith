Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods
#len()
a='python'
len(a)
6
a='python course'
>>> len(a)
13
>>> b=""
>>> len(b)
0
>>> c=" "
>>> len(c)
1
>>> #count
>>> a='powerstar pawankalyan'
>>> a.count("power")
1
>>> a.count('p')
2
>>> #find a string
>>> a='python'
>>> a[1]
'y'
>>> a.find('y')
1
>>> a.find('h')
3
>>> #Escape sequences
>>> #\n->new line
>>> #\t->tab space
>>> a='idno\nname\tmobile\nmailid\nbranch\tcollege
SyntaxError: unterminated string literal (detected at line 1)
>>> a='idno\nname\tmobile\nmailid\nbranch\tcollege'
>>> print(a)
idno
name	mobile
mailid
branch	college
>>> b="id no:034\nname:Lohith\tmobileno:8374793738\nmailid:lohithr618@gmail.com\nbranch:EEE\tcollege:MIC College of tech"
>>> print(b)
id no:034
name:Lohith	mobileno:8374793738
mailid:lohithr618@gmail.com
branch:EEE	college:MIC College of tech
