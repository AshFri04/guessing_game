"""A number-guessing game."""
import random
def number_guessing_game():
    print "Hi! Welcome to the Guessing Game!!"
    name = raw_input("What is your name? ")
    secret_number = random.randint(1, 100)
    guess = 0
    count = 0
    while(guess != secret_number):
        guess = raw_input("Your guess? ")
        try:
            guess_try_int = float(guess).is_integer()
            guess = int(guess)
            if guess in range (1, 100):
                count += 1
                give_hints(guess, secret_number, name, count)
            else:
                print "Oops! Valid numbers are integers between 1-100. Please guess again within the integer range."
        except:
            print "Oops! Please enter a valid integer in range 1-100."
            
def give_hints(guess, secret_number, name, count):
    if guess > secret_number:
        print "Your guess is too high, try again."
    elif guess < secret_number:
        print "Your guess is too low, try again."
    else:
      print "Well done, {}! You found my number in {} tries!".format(name, count)
      ask_to_play_again()


def ask_to_play_again():
  answer = raw_input("Would you like to play again? Y/N")
  if answer == "Y":
    number_guessing_game()
  elif answer == "N":
    print "OK, bye!"
    return None
  else:
    print "I'm sorry, I didn't quite catch that. Please enter Y or N."
    ask_to_play_again()


number_guessing_game()

