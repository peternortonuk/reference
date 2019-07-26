
# works for any iterable
lst = [2, 6, 3, 9, 2]
sorted(lst)

# sorts in place
lst.sort()
print(lst)

a = ['aaa', 'b']
b = ['xxxx', 'y', 'z']

# this is the same as extend
x = a + b
print(x)

# modify list in place
a.append(b)  # add b as a single element ie nest the list
a.extend(b)   # add the contents of b as many elements
print(a)

# apply '+' operator using sum
lists = [['aaa', 'b'], ['xxxx', 'y', 'z']]
x = sum(lists, [])
print(x)

pass