'''
decorator function is built to accept a passed function
without syntactic sugar, we pass our new function to the decorator and get an
enhanced function returned back. we can then run this new function

with syntactic sugar, we run in one line
'''

# ==============================================================================
# simple decorator function


def my_decorator(fn):

    def wrapper():
        print("Before function is called")
        fn()
        print("After function is called")

    return wrapper


# without sugar
def just_some_function1():
    print("Wheee!")


# with sugar
@my_decorator
def just_some_function2():
    print("Whooo!")


# ==============================================================================
# chained decorator

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"


# ==============================================================================
# decorator with arguments
# need an extra nested function to accept passed function

def decorator_with_args(arg1, arg2, arg3):

    def wrap(fn):
        print "Inside wrap()"  # this doesn't execute!

        def wrapped_f(*args):  # a1, a2, a3, a4
            print "Inside wrapped_f()"
            print "Decorator arguments:", arg1, arg2, arg3
            fn(*args)
            print "After f(*args)"
        return wrapped_f

    return wrap


@decorator_with_args("hello", "world", 42)
def say_hello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4


# ==============================================================================
if __name__ == "__main__":

    # ==========================================================================
    # simple decorator function

    # without sugar
    f1 = my_decorator(just_some_function1)
    f1()

    # with sugar
    just_some_function2()

    # ==========================================================================
    # chained decorator
    print hello()

    # ==========================================================================
    # decorator with arguments

    say_hello("say", "hello", "argument", "list")

    pass
