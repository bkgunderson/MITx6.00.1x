print("Please think of a number between 0 and 100!")
acceptable = ['h','l','c']
high = 101
low = 0
guess = int((high + low)/2.0)

while True:
    response = raw_input("Is your secret number " + str(guess) + "? \n Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response not in acceptable:
        print("Sorry, I did not understand your input.")
    elif response == 'l':
        low = guess
        guess = int(low + ((high - low) / 2.0))
    elif response == 'h':
        high = guess
        guess = int(high - ((high - low) / 2.0))
    else:
        break

print("Game over. Your secret number was: %r" % guess)
