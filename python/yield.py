'''
https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

'''

'''
# example 1
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)


# example 2
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
mygenerator = createGenerator() # create a generator object
for i in mygenerator:
    print(i)
'''

# example 3
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
print(iter_curves.next())
print(iter_curves.next())
print(iter_curves.next())
print(iter_curves.next())
print(iter_curves.next())



def cumsum(lst):
    result = 0
    import pdb; pdb.set_trace()
    iter_ = iter(lst)
    while True:
        result += iter_.next()
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
print(it.next())
print(it.next())
print(it.next())
print(it.next())


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