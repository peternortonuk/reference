'''
based on this: https://docs.python.org/2/library/re.html


'''

import re

'''
7.2.5.3. search() vs. match()
Python offers two different primitive operations based on regular expressions: 
   re.match() checks for a match only at the beginning of the string, while 
   re.search() checks for a match anywhere in the string.
'''

pattern = 'oO'
string = 'foo bar'
result = re.search(pattern, string, re.IGNORECASE)
print(result.group())

pattern = r'(?P<first_name>\w+) (?P<last_name>\w+)'
string = 'Malcolm Reynolds'
result = re.search(pattern, string)
print(result.group())
print(result.groupdict())


pass
