# This is a guess the number game.
import random

print('Yoyoyo. Whats your name cuz?')
name = input()

print('Fosho, '+ name +'. Ive got a number on my mind cuz.')
secretNumber = random.randint(1,20)

for guessesTaken in range (1, 7):
    print('Take a guess cuz.')
    guess = int(input())

    if guess < secretNumber:
        print('Yo homie, try a little higher.')
    elif guess > secretNumber:
        print('Yo homie, try a little lower.')
    else:
        break

if guess == secretNumber:
    print('Good job, ' + name + '! You got the juice in ' + str(guessesTaken) + ' tries.')
else: 
    print('Nope. Challenge failed homie. I was thinking of ' + str(secretNumber) + '.')
    
