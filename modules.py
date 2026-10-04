#Difference between module,library and package
'''
Module -> a module is a single python file it consist of a python code
         a module contains variables,functions,and classes
         examples of module sunch as my_module.py , math.py ,random.py

package -> a package contains collections of modules is called package
         ex- requests , numpy  , pandas

library -> a library consists both  modules and packages
         ex- numpy , pandas, django , matplotlib'''

#Note:
'''
Every python file is a module and import is a keyword
Every python file save internally with variable name as "'''



'''def greetings(names):
    print("welcome",names)'''


''''a=10
b=20
print("sum is",a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

#details={"id nos":[10,20,30],"names":["lohith","hamanth","krishna"],"marks":[20,30,40]}

'''if __name__=="__main__":
    a=[10,20,30,40,50,60]
    a.append("code")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("this program is run by script")
    else:
        print("this program is run by module")
dummy()'''

#math maodule
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(4))
print(math.pow(2,4))
print(math.log(10))
print(math.cos(60))
print(math.tan(45))
print(math.ceil(3.9))
print(math.ceil(9.12))
print(math.floor(6.9))'''

#from keyword
from math import pi,log,sqrt,tan
print(pi,log(2),sqrt(10),tan(45))
