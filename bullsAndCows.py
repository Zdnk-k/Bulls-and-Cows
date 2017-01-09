from random import randint, choice


def get_number():
    """ Returns a number to guess """
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #list of digits to choose from
    a = str(randint(1, 9))
    digits.remove(a)
    number = a

    for i in range (0, 3):
        #chooses one of the numbers froom list nd removes it from the list
        a = (choice(digits))
        number += a
        digits.remove(a)

    return number


def player_turn(number):
    """
    players turn,
    asks for an input from player and checks if it's valid,
    returns the result of compare_number()
    """
    guess = input("Your guess: ")

    if not guess.isdigit():     #checks if number
        print("That's not a number!")
    elif len(guess) != 4:       #checks the length
        print("Number must have 4 digits, try again: ")
    else:
        return compare_number(number, guess)


def compare_number(number, guess):
    """
    compares the number to be guessed with number from player
    counts cows and bulls and prints the result
    returns True if numbers are equal (if bulls == 4), False otherwise
    """
    cows = 0
    bulls = 0
    #checks the number
    for i in range (4):
        if number[i] in guess:
            if guess[i] == number[i]:
                bulls += 1
            else:
                cows += 1

    if not bulls == 4:
        print("Cows: %d, Bulls:  %d"  % (cows, bulls))
    return bulls == 4


def game():
    """
    game function
    """
    print("Hey! Got a number for you! Guess what it is!")
    number = get_number()

    print (number)

    win = False
    of_guesses = 0
    while not win:
        win = player_turn(number)
        of_guesses += 1
    print('You done it you lucky bastard! Guesses: %d' % of_guesses)


game()

# TODO: CLASSSES???
# TODO: pydoc
# TODO: guesses
# TODO: map as strings
