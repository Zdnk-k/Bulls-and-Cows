from random import randint, choice

def get_number():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #lsit of digits to choose from
    number = []     #number to guess
    number.append(randint(1, 9))
    digits.remove(number[0])

    for i in range (0, 3):
        #chooses one of the numbers froom list a nd removes it from the list
        number.append(choice(digits))
        digits.remove(number[i + 1])

    return number

def player_turn(number):
    guess = input("Your guess: ")
    if not guess.isdigit():
        print("Enter a number dumbass")
    elif len(guess) != 4:
        print("Number has less or more digits")
    else:
        return check_number(number, guess)


def check_number(number, guess):
    cows = 0
    bulls = 0
    for i in range (4):
        if int(guess[i]) in number:
            if int(guess[i]) == number[i]:
                bulls += 1
            else:
                cows += 1

    if not bulls == 4:
        # print('You got it lucky bastard!')
    # else:
        print("Cows: %d, Bulls:  %d"  % (cows, bulls))
        # print('Cows: {0:2d} Bulls: {1:2d}'.format(cows, bulls))
    return bulls == 4


def list_as_string(number):
    print (''.join(map(str, number)))


def test():
    numbers = []
    for i in range (1, 50):
        a = []
        a = get_number()
        list_as_string(a)
        numbers.append(get_number())

    for l in numbers:
        l = set(l)

    for x in numbers:
        if len(x) != 4:
            print("FUUCK")
        list_as_string(x)

def game():
    print("Hey fucker! Got a number for you! Guess what it is!")
    win = False
    ofGuesses = 0
    number = get_number()
    list_as_string(number)

    while not win:
        win = player_turn(number)
        ofGuesses += 1
    print('You done it you lucky basard! Guesses: %d' % ofGuesses)

game()

# test()
