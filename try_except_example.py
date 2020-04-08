def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        if int(numCats) > 0:
            print('That is not that many cats.')
        elif int(numCats) == 0:
            print('That is no cats.')
        elif int(numCats) < 0:
            print('You cant have negative cats!')
        
except ValueError:
    print('You did not enter a number')
    
