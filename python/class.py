
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

# ==============================================================================
# Inheritance

class Parent(object):
    def __init__(self, value):
        self.value = value

    def spam(self):
        print('Parent spam', self.value)

    def grok(self):
        print('Parent grok')
        self.spam()

class Child1(Parent):
    def yow(self):
        print('Child1 yow')

class Child2(Parent):
    def spam(self):
        print('Child2 spam', self.value)

class Child3(Parent):
    def __init__(self, i):
        super(Child3, self).__init__(i)
        self.value = i

    def spam(self):
        print('Child3 spam', self.value)
        super(Child3, self).spam()


# ==============================================================================
if __name__ == "__main__":
    # need to instantiate the object first
    print A().f(3)

    # don't need the object, just the class
    print B.f(4)
    print C.f(5)

    print('===== Instantiating and attributes =====')
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

    print('===== Inheritance =====')
    p = Parent(25)
    p.spam()
    p.grok()

    c1 = Child1(35)
    print(c1.value)
    c1.yow()
    c1.spam()

    c2 = Child2(45)
    print(c2.value)
    c2.spam()

    c3 = Child3(55)
    print(c3.value)
    c3.spam()


    pass