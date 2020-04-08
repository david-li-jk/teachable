# strings are immutable, specific indexes cannot be changed
name = 'Zophie a cat'
name = name[0:7] + 'the' + name[8:12] # a workaround to change strings

spam = 42
cheese = spam
spam = 100
# cheese will still evaluate to 42

ham = list(range(0,6))
cheese = ham
cheese[1] = 'Hello!'
# ham[1] will evaluate to 'Hello!'

# Immutable items do not have assignment issues like this, as they can't be
# modified "in place". They can only be replaced by new values

def eggs(jeez):
    jeez.append('Bye')

eggs(ham)
print(ham)
# lists point to a location which holds data in list. This means that
# mutable items can 'transcend' global/local scope rules

import copy
beans = ['A', 'B', 'C', 'D']
peas = copy.deepcopy(beans)
peas.append('E')
print('peas: ', end='')
print(peas)
print('beans: ', end='')
print(beans)

# This code copies the actual values from one list to another.
# This means that when peas is appended, it only affects peas
# and not beans.

print('Four score and seven' + \    # line continuation is used to stretch 
      ' years ago')                 # python code across multiple lines
