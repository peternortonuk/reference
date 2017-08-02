
# ==============================================================================
# Classes and methods

class A(object):
    def f(self, x):
        return x+1

class B(object):
    @staticmethod
    def f(x):  # note self not required
        return x+1

class C(object):
    @classmethod
    def f(cls, x):  # we can use other features of the class
        return x+1


# ==============================================================================
# Instantiating and attributes

class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, x):
        self.shares -= x



if __name__ == "__main__":
    # need to instantiate the object first
    print A().f(3)

    # don't need the object, just the class
    print B.f(4)
    print C.f(5)

    # instantiate the object
    h = Holding('AA', '2007-06-11', 100, 32.2)

    # we can call a method in separate stages
    m = h.sell
    m(25)
    print h.shares

    # only has get, set & delete for attributes
    print(getattr(h, 'name'))
    setattr(h, 'name', 'blahh')
    print(getattr(h, 'name'))



    pass