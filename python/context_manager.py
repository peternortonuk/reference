'''
https://www.geeksforgeeks.org/context-manager-in-python/
https://realpython.com/courses/python-context-managers-and-with-statement/

When creating context managers using classes, user need to ensure that the class has the methods:
   __enter__()... returns the resource that needs to be managed
   __exit__()... does not return anything but performs the cleanup operations.
'''

class ContextManager():
    def __init__(self):
        self.print_message = 'init method called'

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


with ContextManager() as manager:
    print(manager.print_message)



'''
https://docs.python.org/3/library/contextlib.html

The function being decorated must return a generator-iterator when called. 
This iterator must yield exactly one value, which will be bound to the targets 
in the with statement’s as clause, if any.
'''

from contextlib import contextmanager


def acquire_resource():
    return 1


def release_resource(resource):
    pass


@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)


with managed_resource(timeout=3600) as resource:
    pass

