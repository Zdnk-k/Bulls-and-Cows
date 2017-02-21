"""
Bulls and cows game
by Zdenko Klain <zdenkoklain@gmail.com>
"""

from random import randint, choice
import sys


def get_number():
    """ Returns a number to guess """
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # list of digits to choose from
    digit = randint(1, 9)  # choose first  digit
    number = digit
    digits.remove(digit)
    for i in range(3):  # choose and removes one of the numbers from list
        digit = (choice(digits))
        number = number * 10 + digit
        digits.remove(digit)
    return number


def player_turn(number):
    """
    asks for an input from player and checks if it's valid,
    if so, returns the result of compare_number()
    """
    guess = input("Your guess: ")
    while not correct_input(guess):  # asks for input from player until its correct
        guess = input("Try again: ")
    return compare_number(number, guess)  # compares numbers


def correct_input(number):
    """
    checks if user input is valid
    """
    if not number.isdigit():     # checks if number
        print("That's not a number!")
        return False
    elif len(number) != 4:       # check length
        print("The number must have 4 digits!")
        return False
    elif not check_digits(number):   # check if 4 different digits
        print('The number must consist of 4 different digits!')
        return False
    else:
        return True


def check_digits(number):
    """
    checks whether the number consists of 4 different digits
    """
    used_digits = set(number)   # creates set from string
    return len(used_digits) == 4    # checks if the set has 4 elements


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

    if bulls != 4:
        print("Bulls: {}, Cows: {}\n".format(bulls, cows))
    return bulls == 4


def how_good(guesses):
    """
    returns a comment on how well the player played
    (according to the number of guesses)
    """
    if guesses < 3:
        return "What sort of sorcery is this!?"
    elif guesses <= 10:
        return "Terrific!"
    elif guesses <= 15:
        return "Jolly good Sir!"
    elif guesses <= 20:
        return "Good job!"
    elif guesses <= 30:
        return "You can do better!"
    elif guesses <= 40:
        return "Oh. maan! Can\'t be that hard!"
    else:
        return "That is rather emberassing..."


def wanna_play():
    """
    asks player whether to play again
    """
    play_again = input('Would you like another round? (yes/no) ')
    while True:  # asks until correct answer
        if play_again in ('Yes', 'yes', 'y', 'YES', 'yep', 'yarp', 'aye'):
            return True
        elif play_again in ('No', 'no', 'n', 'nope', 'NO', 'nay'):
            return False
        else:
            print('God dammit Sir, can you even type??')
            play_again = input('Do you wish to play again???')


def round():
    """
    playes one round of the game
    """
    number = get_number()
    print("Hey! Got a number for you! Guess what it is!")
    win = False
    of_guesses = 0
    while not win:
        win = player_turn(number)
        of_guesses += 1
    print('You\'ve found it in {} guesses. {} '.format(of_guesses, how_good(of_guesses)))


def game():
    """
    plays rounds as long as the player wants to play
    """
    next_round = True
    while next_round:
        round()
        next_round = wanna_play()
    sys.exit()


def menu():
    print("Welcome to Bulls \'n Cows game!\n")
    user_command = menu_input()
    while user_command == 'h':
        print_bnc_help()
        user_command = menu_input()
    if user_command == 'q':
        sys.exit()
    else:
        print('Starting new Game! Good luck!')
        game()


def print_menu_info():
    print("Commands:\n \'n\' for new game, \n \'h\' for help\n \'q\' to quit")


def menu_input():
    print_menu_info()
    inpt = input(">> ")
    while not correct_menu_inpt(inpt):
        inpt = input("Unknown command! Try again!\n>> ")
    return inpt.lower()


def correct_menu_inpt(inpt):
    return inpt in ('n', 'N', 'h', 'H', 'q', 'Q')


def print_bnc_help():
    print("\nHOW TO PLAY!\n"
          "Your objective is to find a 4-digit computer generated secret number.\n"
          "All of the numbers digits are unique.\n"
          "In each turn you input a number.\n"
          "You hit Bull, if digits are on it\'s right position,\n"
          "Cow, if the digitss are in different positions\n")


def bulls_n_cows():
    menu()


bulls_n_cows()