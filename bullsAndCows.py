from random import randint, choice

"""
returns a number to guess
"""
def get_number():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #list of digits to choose from
    a = randint(1, 9)
    digits.remove(a)
    number = str(a)

    for i in range (0, 3):
        #chooses one of the numbers froom list nd removes it from the list
        a = (choice(digits))
        number += str(a)
        digits.remove(a)

    return number

"""
players turn
asks for a input from player and checks if it's valid
calls compare_number()
returns the result of compare_number()
"""
def player_turn(number):
    guess = input("Your guess: ")

    if not guess.isdigit():     #checks if number
        print("Enter a number dumbass")
    elif len(guess) != 4:       #checks the length
        print("Number has less or more digits")
    else:
        return compare_number(number, guess)

"""
compares the number to be guessed with number from player
counts cows and bulls and prints the result
returns True if numbers are equal (if bulls == 4), False otherwise
"""
def compare_number(number, guess):
    cows = 0
    bulls = 0
    #checks the number
    for i in range (4):
        # if int(guess[i]) in number:
        if guess[i] in number:
            # if int(guess[i]) == number[i]:
            if guess[i] == number[i]:
                bulls += 1
            else:
                cows += 1

    if not bulls == 4:
        print("Cows: %d, Bulls:  %d"  % (cows, bulls))
    return bulls == 4


"""
game function
calls get_number()

"""
def game():
    print("Hey fucker! Got a number for you! Guess what it is!")
    number = get_number()

    print (number) '''DEBUG'''

    win = False
    ofGuesses = 0
    while not win:
        win = player_turn(number)
        ofGuesses += 1
    print('You done it you lucky basard! Guesses: %d' % ofGuesses)


#
game()


# TODO: CLASSSES???
# TODO: pydoc
# TODO: guesses
# TODO: map as strings
