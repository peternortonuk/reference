
# nested function; argument scope includes nested function
def foo(arg1, arg2):
    def bar():
        print(arg1, arg2)
    bar()


# nested function returning function
def ham(arg1, arg2):
    def spam():
        print(arg1, arg2)
    return spam

# ==============================================================================
import pdb; pdb.set_trace()

foo('hello', 'world')

x = ham('hello', 'world')
x()

pass

