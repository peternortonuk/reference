
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


x = {'shares': 100, 'date': '2007-06-11', 'name': 'AA', 'price': 32.2}
h = Holding(**x)

# attributes held as a dict on the object
print h.__dict__
h.shares = 50
print h.__dict__

# methods held as a dict on the class
print Holding.__dict__
print Holding.__dict__['cost'](h)



pass
