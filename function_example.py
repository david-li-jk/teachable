def hello(name):
    print('Yoyoyo ' + name)

def plusOne(number):
    return number + 1

hello('Penny')
hello('Yanny')
hello('Manny')

newNumber = plusOne(5)
hello(str(newNumber))


print('Yoyoyo')
print('Mama')

print('Yoyoyo', end='')
print('Mama', end=' ')
print('!')


print('Yoyoyo', 'Mama')
print('Yoyoyo', 'Mama', sep='!')
