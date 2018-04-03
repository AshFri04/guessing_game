"""A number-guessing game."""
import random
def number_guessing_game():
    print "Hi! Welcome to the Guessing Game!!"
    name = raw_input("What is your name? ")
    secret_number = random.randint(1, 100)
    print "Secret number:", secret_number
    guess = 0
    count = 0
    while(guess != secret_number):
        guess = int(raw_input("You guess? "))
        count += 1
        if guess > secret_number:
            print "Your guess is too high, try again."
        elif guess < secret_number:
            print "Your guess is too low, try again."
        else:
            print "Well done, {}! You found my number in {} tries!".format(name, count)
number_guessing_game()