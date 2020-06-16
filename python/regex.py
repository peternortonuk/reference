'''
based on this: https://docs.python.org/2/library/re.html
'''
import re


'''
7.2.5.3. search() vs. match()
Python offers two different primitive operations based on regular expressions: 
   re.match() checks for a SINGLE match only at the BEGINNING of the string, while 
   re.search() checks for a SINGLE match ANYWHERE in the string.
'''

pattern = r'oO'
string = 'foo bar'
result = re.search(pattern, string, re.IGNORECASE)
print(result.group())
print('.........\n')



'''
findall() matches ALL occurrences of a pattern, not just the first one as search() does:
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
basic regex
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

'''

pass
