# List is a value that contains values

spam = [['cat', 'bat', 'rat', 'elephant'],[10, 20, 30, 40,50]]

del spam[1]
del spam[0][2]

'bat' in spam[0] # returns True
'rat' in spam[0] # returns False

'bat' not in spam # returns False
'rat' not in spam[0] # returns True

len(spam[0]) # returns 3
len(spam) # returns 1
