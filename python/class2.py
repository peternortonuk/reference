
'''
https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
'''


class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)

a=A()

'''
classmethods:
the class of the object instance is implicitly passed as the first argument instead of self.
'''
a.class_foo(1)
A.class_foo(1)


'''
staticmethods:
neither self (the object instance) nor  cls (the class) is implicitly passed as the first argument. 
They behave like plain functions except that you can call them from an instance or the class:
A staticmethod isn't useless - it's a way of putting a function into a class (because it logically belongs there), 
while indicating that it does not require access to the class
'''
a.static_foo(1)
A.static_foo('hi')


'''
methods:
foo is just a function, but when you call a.foo you don't just get the function, you get a "partially applied" version 
of the function with the object instance a bound as the first argument to the function. 
foo expects 2 arguments, while a.foo only expects 1 argument; a is bound to foo. 
'''
print(a.foo)
print(a.class_foo)
print(a.static_foo)