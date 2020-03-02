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
