'''
a decorator function accepts a function as an argument and returns a modified function

without syntactic sugar, we pass our function to the decorator and get an
enhanced function returned back; we can then run this new function

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


def my_decorator_with_args(*args):
    return my_decorator


# without sugar
def just_some_function1():
    print("Wheee!")


# with sugar
@my_decorator
def just_some_function2():
    print("Whooo!")


# with args
@my_decorator_with_args(1, 2)
def just_some_function3():
    print("Whaaa!")


# ==============================================================================
# chained decorator

def makebold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper


def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper


@makebold
@makeitalic
def hello():
    return "hello world"


# ==============================================================================
# decorator with arguments
# need an extra nested function because first job is to return
# function without args

def decorator_with_args(arg1, arg2, arg3):

    def wrap(fn):
        print "Inside wrap()"  # executes when function is constructed

        def wrapper(*args):  # a1, a2, a3, a4
            print "Inside wrapped_f()"
            print "decorator_with_args arguments:", arg1, arg2, arg3
            fn(*args)
            print "After f(*args)"
        return wrapper

    return wrap


@decorator_with_args("hello", "world", 42)
def say_hello(a1, a2, a3, a4):
    print 'say_hello arguments:', a1, a2, a3, a4


# ==============================================================================
if __name__ == "__main__":

    print('===== simple decorator function =====')

    # without sugar
    f1 = my_decorator(just_some_function1)
    f1()

    # with sugar
    just_some_function2()

    # with args
    just_some_function3()

    print('===== chained decorator =====')
    print hello()

    print('===== decorator with arguments =====')

    say_hello("say", "hello", "argument", "list")

    pass
