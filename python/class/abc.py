'''
https://www.python-course.eu/python3_abstract_classes.php

Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared,
but contains no implementation.

Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods.

Subclasses of an abstract class in Python are not required to implement abstract methods of the parent class.
'''

from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass


class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value + 42


class DoMul42(AbstractClassExample):
    def do_something(self):
        return self.value * 42

import pdb; pdb.set_trace()

x = DoAdd42(10)
y = DoMul42(10)
print(x.do_something())
print(y.do_something())

