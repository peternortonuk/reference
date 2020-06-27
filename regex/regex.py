'''
sources:
https://docs.python.org/3/library/re.html
https://realpython.com/regex-python/
https://realpython.com/regex-python-part-2/
https://regex101.com/
'''
import re


'''
7.2.5.3. search() vs. match()
Python offers two different primitive operations based on regular expressions: 
   re.match() checks for a SINGLE match only at the BEGINNING of the string, while 
   re.search() checks for a SINGLE match ANYWHERE in the string.
returns a match object in both cases
'''

pattern = r'oO'
string = 'foo bar'
result = re.search(pattern, string, re.IGNORECASE)
print(result)
print('.........\n')


'''
re.findall() matches ALL occurrences of a pattern, not just the first one as search() does
returns a list object only
'''

pattern = r'\w+ly'
string = "He was carefully disguised but captured quickly by police."
result = re.findall(pattern, string)
print(result)
print('.........\n')


'''
simple group
(...) Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; 
the contents of a group can be retrieved after a match has been performed

named group
(?P<name>...) Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name name. 
'''

pattern = r'(?P<first_name>\w+) (?P<last_name>\w+)'
string = 'Malcolm Reynolds'
result = re.search(pattern, string)

print(result.group(0))  # has a special meaning; return all of it
print(result.group(1))
print(result.group(2))

print(result.groups())

print(result.groupdict())
print('.........\n')


'''
Lookahead and Lookbehind Assertions
Don’t consume any of the search string and aren’t part of the returned match object.
(?=<lookahead_regex>)
(?<=<lookbehind_regex>)
'''

pattern = 'foo(?=[a-z])'  # must be followed by a lower case alphabetic letter
string = 'foobar'
result = re.search(pattern, string)
print(result)

string = 'foo123'
result = re.search(pattern, string)
print(result)
print('.........\n')


'''
Substitute
re.sub(<regex>, <repl>, <string>, count=0, flags=0)
Replaces portions of a search string that match a specified regex
'''

pattern = r'\d+'
replace = '#'
string = 'foo.123.bar.789.baz'
result = re.sub(pattern, replace, string)
print(result)
print('.........\n')


'''
Split
re.split(<regex>, <string>, maxsplit=0, flags=0)
splits <string> into substrings using <regex> as the delimiter and returns the substrings as a list.
'''

pattern = r'\d+'
string = 'foo.123.bar.789.baz'
result = re.split(pattern, string)
print(result)
print('.........\n')


'''
cheat sheet
===========

'.' match any character except a newline... if the DOTALL flag has been specified also matches a newline
'*' match 0 or more repetitions
'+' match 1 or more repetitions
'?' match 0 or 1 repetitions

*?, +?, ?? 
the '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. Sometimes this behaviour isnt desired; 
Adding ? after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched. 
Using the RE <.*?> will match only <a>... if the RE <.*> is matched against <a> b <c>, it will match the entire string, and not just <a>. 

'[]' match a set of characters eg [amk] will match 'a', 'm', or 'k'
'^' match the start of the string; also is a complement
'$' match the end of the string
'|' match either one or another regex eg A|B
{m} match exactly m copies
{m,n} match between m and n copies
(...) match whatever is inside the parentheses and indicates the start and end of a group
(?P=name) a reference to a named group; it matches whatever text was matched by the earlier group named name.
(?=...) matches but doesnt consume any of the string... called a LOOKAHEAD ASSERTION eg Isaac (?=Asimov) will match 'Isaac ' only if its followed by 'Asimov'... note also lookbehind, negative lookahead etc

'\d' match any decimal digit; equivalent to the set [0-9]
'\s' match any whitespace character... has the complement '\S'
'\w' match any alphanumeric character and the underscore; equivalent to the set [a-zA-Z0-9_]... has the complement '\W'
'\A' match the start of the string
'\Z' match the end of the string
r'\b' match a word boundary... has the complement '\B'

Raw string notation (r"text") keeps regular expressions sane. Without it, every backslash ('\') in a regular expression 
would have to be prefixed with another one to escape it. 

'''

pass
