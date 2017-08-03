'''
decorator function is built to accept a passed function
without syntactic sugar, we pass our new function to the decorator and get an
enhanced function returned back. we can then run this new function

with syntactic sugar, we run in one line

'''

# ==============================================================================
# simple decorator function

def my_decorator(some_function):

    def wrapper():
        print("Something is happening before some_function() is called.")
        some_function()
        print("Something is happening after some_function() is called.")

    return wrapper


# without sugar
def just_some_function1():
    print("Wheee!")


# with sugar
@my_decorator
def just_some_function2():
    print("Whooo!")



# ==============================================================================
# simple decorator function

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

print hello()







# ==============================================================================
if __name__ == "__main__":
    # without sugar
    f1 = my_decorator(just_some_function1)
    f1()

    # with sugar
    just_some_function2()

    pass