"""
this demonstrates the order of execution
the function and class method are decorated at compile time
so we actually see the decorator print statement FIRST
but NOT the function/method print statements UNTIL the script is run

... also note that the decorator isnt actually modifying the function here
"""


def decorator(fn):
    print(f"{fn.__name__} has been decorated!")
    return fn


@decorator
def func():
    print("Func is running!")


class MyObject(object):
    @decorator
    def my_method(self):
        print("my_method is running!")


if __name__ == '__main__':
    print('=============================')
    print('start running the script here')
    obj = MyObject()
    obj.my_method()

