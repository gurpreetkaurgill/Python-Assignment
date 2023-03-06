import random

secret_number = random.randint(0,100)
tries = 0
max_tries = 10
print('Guess number between 0 and 100.\nYou have maximum 10 chances')
while tries < max_tries:
    guess = int(input('Make guess: '))
    tries += 1
    if guess == secret_number:
        print("You won the game!")
        print(f'You took {tries} tries.')
        exit()
    else:
        if guess > secret_number:
            print('Its greater than secret number')
        elif guess < secret_number:
            print('Its smaller than guess number')
else:
    print(f'You lost the game. The correct answer was {secret_number}')