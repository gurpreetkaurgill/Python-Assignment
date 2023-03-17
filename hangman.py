import random
import string

def guess():
    guess = input('Enter one alphabet:')
    return guess

def str_to_list(word):
    mylist = []
    for i in word:
        mylist.append(i)
    return mylist

def printlist(mylist):
    word = ''
    for i in mylist:
        word += i
    return word

def update_list(mystring , random_word, myguess):
    for i in range (0, len(random_word)):
        if random_word[i] == myguess and mystring[i] == '_':
            mystring[i] = random_word[i]
    return mystring

def is_complete(mystring):
    for i in mystring:
        if i == '_':
            return False
    return True

def display_remainings(guessed_letter):
    a_to_z = string.ascii_lowercase
    remainings = ''
    for i in a_to_z:
        if i not in guessed_letter:
            remainings += i
    return remainings


def play_game():
    fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

    random_word = str_to_list(random.choice(fruits))
    word_length = len(random_word)
    chances = 10
    mystring = str_to_list(word_length *'_')
    guessed_letters = []

    print('Guess a fruit name')

    while chances > 0:
        if is_complete(mystring):
            print(f"You guess '{printlist(mystring)}' is correct")
            break
        else:
            print(f'\nalready guessed: {printlist(guessed_letters)} \nremaining guess letters: {display_remainings(guessed_letters)}')
            print(printlist(mystring))
            myguess = guess()
            if len(myguess) == 1:
                if myguess in guessed_letters:
                    print('You already guessed that letter')
                elif myguess in random_word:
                    guessed_letters.append(myguess)
                    mystring = update_list(mystring, random_word, myguess)
                else:
                    guessed_letters.append(myguess)
                    chances -= 1
                    print(f'Wrong guess you have {chances} chances left')
            else:
                print('Enter 1 alphabet only')
                guess()

    else:
        print(f"Your lost the game \nThe answer was '{printlist(random_word)}'")




play_again = '1'
while play_again != '2':
    play_game()
    play_again = input('Enter 1 to play again and 2 to exit')
    if play_again == '2':
        break
    else:
        print('Enter correc input')