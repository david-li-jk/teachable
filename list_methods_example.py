spam = ['cat', 'dog', 'bat']
spam.append('moose') # adds entry into list at end of list
spam.insert(1, 'chicken') # inserts into list at specific index number
spam.remove('bat') # removes first entry of a specific string from list
del spam[0] # removes an entry at a specific index

ham = [1, 7, -3, 2.14]
ham.sort() # sorts in ascending order
spam.sort(reverse = True) # sorts in reverse ascending order

#ascending order for letters prioritizes capitalized characters
sausage = ['A', 'z', 'a', 'Z']
sausage.sort(key=str.lower) # assumes keys are lower case, thus ignoring case
# can be fixed by placing a sausage.sort() before the above line
