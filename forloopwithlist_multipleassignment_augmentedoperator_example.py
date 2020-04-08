
spam = list(range(0,100,2)) # returns list of numbers from 0 to 100 in multiples of 2

supplies = ['pens', 'paperclip', 'binders', 'flamethower']
for i in range(len(supplies)): #len(supplies) evals to 4, range(4) evals to 0, 1, 2, 3
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat', 'orange', 'loud'] 
size, color, disposition = cat # multiple assignments, size will return cat[0]

a = 'AAA'
b = 'BBB'
c = 'CCC'
a,b,c = b,c,a # swapping variables

ham = 42
ham += 1 # augmented operators, ham will now return 43
ham -= 1 # ham will now return 42
ham *= 0.5 # ham will now return 21
ham /= 0.5 # ham will now return 42
ham %= 40 # ham will now return 2
