Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Dictionary
a={"name":"pooja","city":"vij"}
print(a)
{'name': 'pooja', 'city': 'vij'}
type(a)
<class 'dict'>
b={"name","lohith"}
type(b)
<class 'set'>

#keys
a={"year":2026,"month":"sep","date":9}
a.keys()
dict_keys(['year', 'month', 'date'])

#values
a.values()
dict_values([2026, 'sep', 9])

#items
a.items()
dict_items([('year', 2026), ('month', 'sep'), ('date', 9)])

a["year"]
2026

a[2026]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a[2026]
KeyError: 2026
a.get("year")
2026

#update
a={"name":"lohith","city":"vij"}
a.update({"mailid":"lohithr618@gamil.com"})
a
{'name': 'lohith', 'city': 'vij', 'mailid': 'lohithr618@gamil.com'}
a.update({"year":2026},{"time":3})
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.update({"year":2026},{"time":3})
TypeError: update expected at most 1 argument, got 2
a.update({"year":2026,"time":3})
a
{'name': 'lohith', 'city': 'vij', 'mailid': 'lohithr618@gamil.com', 'year': 2026, 'time': 3}

#setdefault
a={"hour":3,"min":10}
a.setdefault("sec",4)
4
a
{'hour': 3, 'min': 10, 'sec': 4}
#in setdefault() method we does not give any dict format it consider as first as key and second value

#pop
a={"week":"wed","date":9}
a.pop()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("week")
'wed'
a
{'date': 9}

#popitem
a={"country":"india","state":"ap"}
a.popitem()
('state', 'ap')
a
{'country': 'india'}
>>> 
>>> #copy
>>> a={"name":"lohith","course":"python","duration":100}
>>> a.copy()
{'name': 'lohith', 'course': 'python', 'duration': 100}
>>> len(a)
3
>>> a.count("name")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
>>> a.clear()
>>> a
{}
>>> 
>>> #why count and index are not in dict
>>> a={"name":"lohiht","year":2026,"name":"lohith"}
>>> print(a)
{'name': 'lohith', 'year': 2026}
>>> a={"name":"lohith","year":2026,"name":"reddy"}
>>> print(a)
{'name': 'reddy', 'year': 2026}
>>> a={"name":"lohith","year":2026,"name1":"lohith"}
>>> print(a)
{'name': 'lohith', 'year': 2026, 'name1': 'lohith'}
>>> 
>>> #multiple values
>>> a={"idno":[10,20,30],"names":["lohith","hemanth","kanthu"],"places":["vij","gun","tnl"]}
>>> print(a)
{'idno': [10, 20, 30], 'names': ['lohith', 'hemanth', 'kanthu'], 'places': ['vij', 'gun', 'tnl']}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idno', 'names', 'places'])
>>> a.values()
dict_values([[10, 20, 30], ['lohith', 'hemanth', 'kanthu'], ['vij', 'gun', 'tnl']])
>>> a.items()
dict_items([('idno', [10, 20, 30]), ('names', ['lohith', 'hemanth', 'kanthu']), ('places', ['vij', 'gun', 'tnl'])])
