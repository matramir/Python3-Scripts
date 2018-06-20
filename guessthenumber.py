# python3
#This is a guess the number game
import random
print('Hello, whats is your name?')
name = input()
global guess
guess =0
secretNumber= random.randint(1, 20)
print('Well, ' + name +', I am thinking of a number between 1 and 20.')

#Ask for the player to guess 6 times
for guessestaken in range (1, 7):
    triesLeft = (7- guessestaken)
    print ('Take a guess: You have '+str(triesLeft)+'.')
    try:
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low')
        elif guess > secretNumber:
            print('Your guess is too high')
        else:
            break #this condition is the correct guess
    except ValueError:
        print('Value entered not valid, please enter a number between 1 and 20')

if guess == secretNumber:
    print('Good job, '+name+'! you guessed the number correctly!')
    print('You took '+str(guessestaken)+' guesses.')
else:
    print('Nope. You guessed wrong, the number was '+str(secretNumber))
