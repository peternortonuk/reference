
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
# Simple Inheritance
# 33-8.1 Inheritance Concepts.mp4

class Parent1(object):
    def __init__(self, value):
        self.value = value

    def spam(self):
        #super(Parent1, self).spam()
        print('Parent1 spam', self.value)

    def grok(self):
        print('Parent1 grok')
        self.spam()


class Parent2(object):
    def yow(self):
        print('Parent2 yow')


class Child1(Parent1):
    def yow(self):
        print('Child1 yow')


class Child2(Parent1):
    def spam(self):
        print('Child2 spam', self.value)


class Child3(Parent1):
     def spam(self):
         super(Child3, self).spam()
         print('Child3 spam', self.value)


class Child4(Parent1):
    # if i override the init method then i need to ensure the parent
    # initialisation is supported
    def __init__(self, value, extra):
        super(Child4, self).__init__(value)
        self.extra = extra

    def spam(self):
        print('Child4 spam', self.value)
        super(Child4, self).spam()


class Child5(Parent1, Parent2):
    pass


# ==============================================================================
# Advanced Inheritance
# 35-8.3 Advanced Inheritance.mp4

class ChildMixin(object):
    def spam(self):
        print('Child mixin')
        super(ChildMixin, self).spam()



# ==============================================================================

class Grandchild1(Child2):
    def spam(self):
        #super(Child2, self).spam()
        super(Grandchild1, self).spam()
        print ('Grandchild1 spam')

# ==============================================================================
if __name__ == "__main__":

    print('===== Classes and methods =====')
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

    print('===== Simple Inheritance =====')
    p = Parent1(25)
    p.spam()
    p.grok()

    c1 = Child1(35)
    print(c1.value)
    c1.yow()
    c1.spam()

    c2 = Child2(45)
    print(c2.value)
    c2.spam()

    c3 = Child3(46)
    c3.spam()
    c3.grok()

    c4 = Child4(55, 66)
    print(c4.value)
    c4.spam()

    c5 = Child5(42)
    c5.grok()
    c5.spam()
    c5.yow()

    # shows me the order of super()
    print Grandchild1.__mro__
    g1 = Grandchild1(1)
    g1.spam()

    pass