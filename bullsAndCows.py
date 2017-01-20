"""
Bulls and cows game
by Zdenko Klain <zdenkoklain@gmail.com>
"""

from random import randint, choice


def get_number():
    """ Returns a number to guess """
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #list of digits to choose from
    digit = randint(1, 9) #choose first  digit
    number = digit * 1000
    digits.remove(digit)
    for i in range(3): #choose and removes one of the numbers from list
        digit = (choice(digits))
        number += digit * pow(10, i)
        digits.remove(digit)
    return number


def player_turn(number):
    """
    asks for an input from player and checks if it's valid,
    returns the result of compare_number()
    """
    guess = input("Your guess: ")

    if not guess.isdigit():     #checks if number
        print("That's not a number! Try again: ")
        print("The number must have 4 digits, try again: ")
    else:
        return compare_number(number, guess)


def compare_number(number, guess):
    """
    Compares the number to be guessed with the number from player
    counts cows and bulls and prints the result
    returns True if numbers are equal (if bulls == 4), False otherwise
    """
    cows = 0
    bulls = 0
    for i in range(4):
        number = str(number)
        if number[i] in guess:
            if guess[i] == number[i]:
                bulls += 1
            else:
                cows += 1

    if not bulls == 4:
        print("Cows: %d, Bulls:  %d"  % (cows, bulls))
    return bulls == 4


def how_good(guesses):
    """
    returns a comment on how well the player played according to the number of guesses
    """
    if guesses < 3:
        return "What sort of sorcery is this!?"
    elif guesses <= 5:
        return "Terrific!"
    elif guesses <= 10:
        return 'Jolly good Sir!'
    elif guesses <= 15:
        return 'Good job!'
    elif guesses <= 20:
        return 'Naaaah...You can do better!'
    else:
        return 'Emberassing'


def game():
    """
    creates a number to guess, calls player_turn in while loop until player guesses correcty
    """
    print("Hey! Got a number for you! Guess what it is!")
    number = get_number()
    win = False
    of_guesses = 0
    while not win:
        win = player_turn(number)
        of_guesses += 1
    print('You\'ve found it in %d guesses. %s' % (of_guesses, how_good(of_guesses)))


game()
