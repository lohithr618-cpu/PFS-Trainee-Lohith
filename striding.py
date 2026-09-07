Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a='Cloud Computing'
a[2:13:3]
'o mt'
a[4:14:5]
'dp'
>>> a[3:12:6]
'up'
>>> a='Machine Learning'
>>> a[::3]
'Mheeng'
>>> a[::5]
'Mnag'
>>> a[::2]
'McieLann'
>>> a[::9]
'Me'
>>> a[3:11]
'hine Lea'
>>> a[5:]
'ne Learning'
>>> a[:7]
'Machine'
>>> #Negative Striding
>>> a='python course'
>>> a[-1:-9:-3]
'eu '
>>> a[-2:-12:-4]
'sch'
>>> a[-4:-13:-5]
'uo'
>>> a[-6:-12:-2]
'cnh'
>>> #do's and do not's
>>> a='python course'
>>> a[7:3:2]
''
>>> a[3:7:2]
'hn'
>>> a[-9:-5:-2]
''
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
