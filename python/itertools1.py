'''
https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

'''

# ===================================================================
'''
https://www.python.org/dev/peps/pep-0289/
generator expressions are a high performance, memory efficient generalization of list comprehensions
'''
print('\n=========================================================\n'
      'example 1'
      '\n========\n')

my_generator = (x * x for x in range(3))
for i in my_generator:
    print(i)


# ===================================================================
'''
https://www.python.org/dev/peps/pep-0255/
A function that contains a yield statement is called a generator function.
Generator functions are a special kind of function that return a lazy iterator. 

Each time the next() method of a generator-iterator is invoked, the code in 
the body of the generator-function is executed until a yield statement is encountered.

If a yield statement is encountered, the state of the function is frozen, and the 
value of expression_list is returned to .next()'s caller. By "frozen" we mean that 
all local state is retained, including the current bindings of local variables, 
the instruction pointer, and the internal evaluation stack: enough information is saved 
so that the next time .next() is invoked, the function can proceed exactly 
as if the yield statement were just another external call.
'''
print('\n=========================================================\n'
      'example 2'
      '\n========\n')


def create_generator(iterable):
    for i in iterable:
        yield i*i


my_generator = create_generator(range(3))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))


# ===================================================================
'''
https://realpython.com/lessons/understanding-generators/
https://realpython.com/introduction-to-python-generators/
'''
print('\n=========================================================\n'
      'example 3'
      '\n========\n')


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        yield print("this is the second yield statement")


# ===================================================================
'''
When a return statement is encountered, control proceeds as in any function return, 
executing the appropriate finally clauses (if any exist). Then a StopIteration exception 
is raised, signalling that the iterator is exhausted. A StopIteration exception is 
also raised if control flows off the end of the generator without an explicit return.
'''
print('\n=========================================================\n'
      'example 4'
      '\n========\n')

bookmap = {
    'PROP': {
        'portfolio': 'PROP_OPTIONS_GAS_UK',
        'strategy': '',
        'portfolio_id': 20115,
        'chosenvols': ['VOL_TTF', 'VOL_NBP'],
        'chosencurves': ['NBP', 'TTF'],
        'run_auto_eod': True,
        'run_auto_intraday': True,
        'run_auto_scenarios': True,
    },
}


def all_curves():
    for book, book_config in bookmap.items():
        for curve in book_config['chosencurves']:
            yield curve
            for curve in book_config['chosenvols']:
                yield curve

iter_curves = all_curves()
print(next(iter_curves))
print(next(iter_curves))
print(next(iter_curves))
print(next(iter_curves))
print(next(iter_curves))
import pdb; pdb.set_trace()



def cumsum(lst):
    result = 0
    import pdb; pdb.set_trace()
    iter_ = iter(lst)
    while True:
        result += next(iter_)
        yield result

print(cumsum([1,2,3]))

pass


'''
david beazley: iteration protocol and customisation via generators
saved to google drive
62-14.1
'''

names = ['YHOO', 'IBM', 'AAPL']
for name in names:
    print(name)

# under the hood its doing this...
it = names.__iter__()
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# this is a generator function
def countdown(n):
    print('counting down from ', n)
    while n>0:
        yield n
        n -= 1
    print('done')


# this doesnt do anything except assign the generator function
y = countdown(5)
print(y)

# now the loop iterates through and each step runs the function
for x in y:
    print(x)


# related to a list comprehension
nums = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in nums]
print(squares)

# we have generator expressions
squares = (x**2 for x in nums)
print(squares)


# but they can't be re-used
# one way around this is...
class Countdown(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        print('counting down from ', self.n)
        while self.n > 0:
            yield self.n
            self.n -= 1
        print('done')


c = Countdown(5)
for x in c:
    print(x)
