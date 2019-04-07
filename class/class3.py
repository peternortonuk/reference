'''
Python Programming Language
By David Beazley
Publisher: Pearson
Release Date: August 2016
Duration: 6 hours 26 minutes

Location: Google Drive \Media\Video\Python Programming Language
45-10.1 Instance Representation, Attribute Access and Naming Conventions
'''

class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __repr__(self):
        return 'Holding({!r},{!r},{!r},{!r})'.format(self.name, self.date, self.shares, self.price)

    def __str__(self):
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


from pprint import pprint
import pdb; pdb.set_trace()

x = {'shares': 100, 'date': '2007-06-11', 'name': 'AA', 'price': 32.2}
h = Holding(**x)
print(h)
print

# everything is in a dict so...
# ...attributes are held in the dict
print(h.__dict__)
h.shares = 50
print(h.__dict__)
print

# ... and methods are held there too
pprint(Holding.__dict__)
foo = Holding.__dict__['cost']
print(foo)  # foo is the method
print(foo(h))  # call the method and pass the object as self
print
