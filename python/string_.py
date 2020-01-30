'''
https://realpython.com/python-f-strings/
https://www.python.org/dev/peps/pep-0498/
https://docs.python.org/3.4/library/string.html#format-specification-mini-language
'''


name = 'Eric'
age = 74
long_name = 'Eric Idle'

# =====================
# %-formatting

s = 'Hello, %s. You are %s.' % (name, age)
print(s)

# =====================
# str.format

s = 'Hello, {1}. You are {0}.'.format(age, name)
print(s)

# =====================
# f strings
# aka Literal String Interpolation

s = f'Hello, {name}. You are {age}.'
print(s)


def to_lowercase(input):
    return input.lower()


# call functions directly
s = f'{to_lowercase(long_name)} is funny'
print(s)


for x in (32, 100, 1.000000001):
    print(f'x = {x:+10}')
