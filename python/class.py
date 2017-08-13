
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
    # initialisation is supported explicitly
    def __init__(self, value, extra):
        super(Child4, self).__init__(value)
        self.extra = extra

    def spam(self):
        print('Child4 spam', self.value)
        super(Child4, self).spam()


# demonstrates multiple inheritance
# an object of this type has access to both methods and attributes
# but at this stage there is no conflict ie each method appears only once
class Child5(Parent1, Parent2):
    pass


# ==============================================================================
# Advanced Inheritance
# 35-8.3 Advanced Inheritance.mp4

# a Mixin is intended to provide a piece of functionality common to MANY classes
# its intended to be used alongside other classes and is not standalone
# the Mixin inherits from object but the super method takes its functionality
# from the associated class

class ChildMixin(object):
    def spam(self):
        print('Child mixin')
        super(ChildMixin, self).spam()


# the order here is very important; the base class goes on the right of the arg list
# this is no different to standard mro
# it's just that you want the Mixin to override and call the next in line
# TODO: check this assumption
# TODO: why is there reference to reading right-to-left; it doesn't!
class Child6(ChildMixin, Parent1):
    pass


class Grandchild1(Child2):
    def spam(self):
        print ('Grandchild1 spam')
        super(Grandchild1, self).spam()

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
    print

    c1 = Child1(35)
    print(c1.value)
    c1.yow()
    c1.spam()  # Child1 doesnt have a spam method; so look in Parent1
    print

    c2 = Child2(45)
    print(c2.value)
    c2.spam()  # Child2 does have a spam method; it completely overrides Parent1
    print

    c3 = Child3(46)
    print(c3.value)
    c3.spam()  # Both classes have a spam method but the parent method is called as well using super
    print

    c4 = Child4(55, 66)
    print(c4.value, c4.extra)
    c4.spam()
    print

    c5 = Child5(42)
    print(c5.value)
    c5.spam()  # from Parent1
    c5.grok()  # from Parent1
    c5.yow()  # from Parent2
    print(Child5.__mro__)  # doesn't matter at this stage; there is no overriding
    print


    print('===== Advanced Inheritance =====')
    c6 = Child6(100)
    print(c6.value)
    c6.spam()  # calls the mixin then the next-in-line method; being Parent1
    print(Child6.__mro__)
    print

    # shows me the order of super()
    g1 = Grandchild1(101)
    print(g1.value)
    g1.spam()  # g1.spam calls super; next in line is Child2 where inheritance halts; Parent1 has no spam method
    print Grandchild1.__mro__

    pass