

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

if __name__ == "__main__":
    # need to instantiate the object first
    print A().f(3)

    # don't need the object, just the class
    print B.f(4)
    print C.f(5)

    pass