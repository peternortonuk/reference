'''
Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters
https://www.youtube.com/watch?v=jCzT9XFZ5bw

'''


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


# getter
emp1 = Employee('Peter', 'Norton')
print(emp1.fullname)

# setter
emp1.fullname = 'Bob Hope'
print(emp1.fullname)

# deleter
del emp1.fullname