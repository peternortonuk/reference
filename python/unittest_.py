import unittest
from unittest.mock import Mock

mock = Mock(return_value=6)
print(mock())

def my_func(x):
    return f'hello {x}'

class TestExample(unittest.TestCase):
    def test_blahh(self):
        result = my_func('whatever')
        self.assertEqual(result, 'hello whatever')

'''
>>>python -m unittest unittest_.py
'''