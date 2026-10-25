#Oops
#syntax
'''class classname():
    #attributes
    name="lohiht"
    age=22
    place="vij"
    def fname(method_name):
        print(statements.........)
a=classname()
a.fname()'''

#class declaration
'''class details():
    name="lohith"
    age=22
    place="vij"
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''

#object instantiation
'''class details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.data("lohith",22,"vij")
a.display()
a.data("hemanth",21,"vij")
a.display()
a.data("krishna",22,"tenali")
a.display()
a.data("teja",23,"guntur")
a.display()'''

#object intialization
#__init__
'''class details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details("lohith",22,"vij")
print(dir(a))
a.display()'''

#runtime input
'''class details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details(input("enter name:"),int(input("enter age:")),input("enter place:"))
print(dir(a))
a.display()'''

'''class details():
    #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''

#diff b/w single underscore(_) & double underscore(__)
'''  def -- when user wants to create  a variable in python with double leading underscore(__) our pytho interpreter treats as a spl variable  and
   avoid name conflits methods and inner classes '''

'''class Employee1():
    def __init__(self):
        self.name="lohith"
        self._mailid="lohithr618@gmail.com"
        self.__salary=10000#private variable(__)
class Employee2():
    def __init__(self):
        self.name="hemanth"
        self._mailid="hemanth@mailid"
        self.__salary=15000
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee1__salary)
b=Employee2()
print(dir(b))
print(b.name)
print(b._mailid)
#print(b.__salary)
print(b._Employee2__salary)'''


#polymorphism
#operator overloading
'''a,b=2,4
print(a+b)
print(a.__add__(b))
print(a.__add__(8))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(2))
print(a.__pow__(4))
print(a.__ge__(10))
print(a.__le__(20))
a=[1,2,3,4,5];b=[5,6,7,8,9]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())
print(("lohith").__add__("r").title())'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(10)
y=B(20)
#x=10
#y=40
print(x+y)'''


#15/10
#Method overloding
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None  and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends...........")
a=new()
a.sum()
a.sum(5,4,3)
a.sum(5,4)'''


'''class new():
    def sum(self,a=5,b=4,c=3):
        if a!=4 and b!=5  and c!=2:
            print("the sum is",a+b+c)
        elif a!=4 and b!=2:
            print("the product is",a*b)
        else:
            print("program ends...........")
a=new()
a.sum()'''

#method overriding
'''class animal():
    def speak(self):
        print("anmal can make sounds")
class dog():
    def speak(self):
        print("dog barks")
a=animal()
b=dog()
a.speak()
b.speak()'''

#vehicle
'''class honda():
    def vehicle(self):
        print("pricr is 1.85")
class tvs():
    def vehicle(self):
        print("price is  1.9")
a=honda()
b=tvs()
a.vehicle()
b.vehicle()'''


##..........INHERITANCE............

#single inheritance
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        #print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        #print("new cash is ",cls.cash+cls.cash)
        print("new cash is ",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()'''


#Multi inheritance
'''class Father():
    def height(self):
        print("5.5 inches")
class Mother():
    def weight(self):
        print("60 kgs")
class kid():
    def dob(self):
        print("just born.........")
a=Father()
b=Mother()
c=kid()
a.height()
b.weight()
c.dob()'''

'''class Father():
    def height(self):
        print("5.5 inches")
class Mother():
    def weight(self):
        print("60 kgs")
class kid(Father,Mother):
    def dob(self):
        print("just born.........")
a=kid()
a.height()
a.weight()
a.dob()'''


##.........Multilevel Inheritence..........
'''class Grandparent():
    def land(self):
        print("5 acres")
class parent(Grandparent):
    def house(self):
        print("50 sqft")
class child(parent):
    def car(self):
        print("thar")
a=child()
a.land()
a.house()
a.car()'''

##.......Hierarchical............
# def Hierarchical inheritence is  one parent class is inherited by multiple child classes
'''class Employee():
    def company(self):
        print("TCS")
class trainer(Employee):
    def teach(self):
        print("data")
class developer(Employee):
    def data(self):
        print("code")
a=trainer()
b=developer()
a.company()
a.teach()
b.company()
b.data()'''

#..........Hybrid Inheritence.........
#def -hybrid Inheritence means combining one or more than type of inheritance for ex:hierarchical +multiple
'''class trainer():#parent
    def teach(self):
        print("python")
class developer(trainer):#child -1
    def code(self):
        print("develops the code")
class student(trainer):#child 2
    def study(self):
        print("learns python")
class program_manager(student,developer):
    def work(self):
        print("assigns the work")
a=program_manager()
a.teach()
a.code()
a.study()
a.work()'''

#library management sysytem
'''
1.add book ->pthon 
2.list of book ->display
3.issue book  ->issue book
4.return book  ->return 
5.delete book  ->exit '''


#super ()
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constarctor")
class child(parent):
    def __init__(self,name,city):
        super().__init__(name)
        self.city=city
        print("child constractor")
a=child("lohith","vij")
print(a.name)
print(a.city)'''


#24/10             
#..ENCAPSULATION....
#publicdata
'''DEF- combining multiple units into a single unit is known as encapsulation '''
    

'''class A():
    publicdata=10
    def method1(self):
        print(self.publicdata)
class B(A):
    def method2(self):
        print(self.publicdata)

x=B()
x.method1()
x.method2()'''


#_protecteddata()
'''class A():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class B(A):
    def method2(self):
        print(self._protecteddata)

x=B()
x.method1()
x.method2()
print(x._protecteddata)'''

#__privatedata
'''class A():
    __privatedata="lohith"
    def method1(self):
        print(self.__privatedata)
class B(A):
    def method2(self):
        print(self._A__privatedata)
y=B()
y.method1()
y.method2()'''


#......ABSTRACTION.......
'''def -hiding unnecessary information feom user is called abstraction'''

#abstract class -->one or more abstract methods is called abstract class
#abstract method -->A method is declared without inforamtion is called abstractmethod

'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()'''

'''class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    def method1(self):
        print("python")
obj1=A()
obj1.method1()'''

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()








