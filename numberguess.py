print("Please think of a number between 0 and 100!  ")
acceptable = ['h','l','c']
guess = 50
guessnumber = 1

while True:
    response = raw_input("Is your secret number " + str(guess) + "? \n Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response not in acceptable:
        print("Sorry, I did not understand your input.")
    elif response == 'l':
        guessnumber += 1
        guess = int(guess + (100 / 2**guessnumber))
    elif response == 'h':
        guessnumber += 1
        guess = int(guess - (100 / 2**guessnumber))
    else:
        break

print("Game over. Your secret number was: %r" % guess)
