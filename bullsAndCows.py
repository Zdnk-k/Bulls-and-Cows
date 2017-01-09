from random import randint, choice


def get_number():
    """ Returns a number to guess """
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #list of digits to choose from
    a = randint(1, 9)
    digits.remove(a)
    number = a * 1000;

    for i in range (3, 0, -1):
        """chooses one of the numbers froom list nd removes it from the list"""
        a = (choice(digits))
        digits.remove(a)
        number += a * pow(10, i - 1)

    return number


def player_turn(number):
    """
    asks for an input from player and checks if it's valid,
    returns the result of compare_number()
    """
    guess = input("Your guess: ")

    if not guess.isdigit():     #checks if number
        print("That's not a number you kinky bastard!")
    elif len(guess) != 4:       #checks the length"""
        print("The number must have 4 digits, try again: ")
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
    for i in range (4):
        number = str(number)
        if number[i] in guess:
            if guess[i] == number[i]:
                bulls += 1
            else:
                cows += 1

    if not bulls == 4:
        print("Cows: %d, Bulls:  %d"  % (cows, bulls))
    return bulls == 4

def how_good(g):
    if g <2 :
        return "What sort of sorcery is this!?"
    elif g <= 3:
        return "Terrific!"
    elif g <= 6:
        return 'Joly good Sir!'
    elif g <= 10:
        return 'Good job!'
    elif g <= 15:
        return 'nicht so gut!'
    else:
        return 'Emberassing. You can do better!'


def game():
    """
    game function
    """
    print("Good day to you Sir! Got a fuckin number for you! Fucking guess what it is!")
    number = get_number()

    win = False
    of_guesses = 0
    while not win:
        win = player_turn(number)
        of_guesses += 1
    print('You done it you lucky bastard! Fuckin look at you! What a clever fuck you are! And just in fuckin %d guesses. %s' % (of_guesses, how_good(of_guesses)))


game()

# TODO: guesses
