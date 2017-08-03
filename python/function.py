
# nested function; argument scope includes nested function

def foo(arg1, arg2):
    def bar():
        print(arg1, arg2)
    bar()

foo('hello', 'world')



# nested function returning function

def foo(arg1, arg2):
    def bar():
        print(arg1, arg2)
    return bar

x = foo('hello', 'world')
x()

pass

