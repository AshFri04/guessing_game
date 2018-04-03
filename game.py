"""A number-guessing game."""

def number_guessing_game():
    import random
    print "Hi! Welcome to the Guessing Game!!"
    print "What is your name?: "
    
    name = raw_input(">")
    secret_number = random.randint(1, 101)
    guess = 0
    count = 0

    while(guess != secret_number):
        guess = raw_input("You guess? ")
        if guess > secret_number:
            print "Your guess is too high, try again."
            count += 1
        elif guess < secret_number:
            print "Your guess is too low, try again."
            count += 1
        else:
            print