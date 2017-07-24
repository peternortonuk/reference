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
print iter_curves.next()
print iter_curves.next()
print iter_curves.next()
print iter_curves.next()
print iter_curves.next()
print iter_curves.next()
print iter_curves.next()

pass