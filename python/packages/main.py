'''
https://pythonconquerstheuniverse.wordpress.com/2009/10/15/python-packages/

Just dumping a bunch of modules into a folder doesn't make it a package,
it just makes it a bunch of modules in a folder. Unless that folder is in the PYTHONPATH,
you won't be able to import the modules because Python doesn't look inside folders.
The one exception is that it will look inside a folder for a __init__.py file,
and if it finds one, it will treat that folder and its contents as a package.

'''


# load the .py files as a module
import parrot.fighting
from parrot.feeding import drinking
# module given an alias
from parrot import flying as fl

# load the function
from parrot.feeding.eating import eating
# function given an alias
from parrot.feeding.eating import chomping as ch


# call functions
parrot.fighting.fighting()
drinking.drinking()
fl.flying()
eating()
ch()
