'''
https://leemendelowitz.github.io/blog/how-does-python-find-packages.html

sys.path is populated using the current working directory,
followed by directories listed in your PYTHONPATH environment variable,
followed by installation-dependent default paths,
which are controlled by the site module.

C:\dev\bin\Anaconda\Lib\site.py

So how does the Ubuntu distribution of Python know to use 
/usr/local/lib/python2.7/dist-packages in sys.path? 
It's hardcoded into their site module! 

'''

import sys
import site
from pprint import pprint as pp

# locations that will be searched for imports
pp(sys.path)

# this module modifies the standard path
print(site.__file__)
pass