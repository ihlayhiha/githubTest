import random

guess = int(input("Guess a number between 1 and 10: ")) 

while guess != random.randint(1, 10):
    if guess == 0:
        print('You chose to exit the game')
        break
    guess = int(input("WRONG! Guess again?: "))
print("yay! you guessed it!")