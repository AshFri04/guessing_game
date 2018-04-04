"""A number-guessing game."""
import random
import math


save_scores = []
def number_guessing_game():
    name, secret_number, max_num_guesses, range_diff, low, high = initiate()
    guess = 0
    count = 0
    game_complete = False
    while(not game_complete):
        guess = raw_input("Your guess? ")
        try:
            guess = int(guess)
            if guess in range(low, high+1):
                print "low: ", low, "high+1: ", high+1
                if count < max_num_guesses:
                    count += 1
                    game_complete = give_hints(guess, secret_number, name, count, range_diff)
                else:
                    print "Uh-oh! You ran out of guesses."
                    ask_to_play_again()
            else:
                print "Oops! Valid numbers are integers between {}-{}. Please guess again within the integer range.".format(low, high)
        except:

            print "Oops! Please enter a valid integer in range {}-{}.".format(low, high)



def initiate():
    print "Hi! Welcome to the Guessing Game!!"
    name = raw_input("What is your name? ")
    low, high = get_range()
    range_diff = (high+1) - low
    max_num_guesses = int(math.sqrt(range_diff + 1))
    print "Low:", low, "High:", high
    secret_number = random.randint(low, high)
    print "Secret number: ", secret_number
    print "Let's go! You have only {} tries to guess my secret number so try your best!".format(max_num_guesses)
    return name, secret_number, max_num_guesses, range_diff, low, high

def get_range():
    range = raw_input("The default range is 1-100. Press enter to accept or enter a custom range: ") or "1-100"
    try:
        result = tuple(map(lambda x: int(x), range.split('-')))
        if result[0] == result[1]:
            print "Oops! That is not a valid range. Please try again."
            get_range()
        else:
            return result[0], result[1]
    except:
        print "Oops! That is not a valid range. Please try again."
        get_range()

def give_hints(guess, secret_number, name, count, range_diff):
    if guess > secret_number:
        print "Your guess is too high, try again."
        return False
    elif guess < secret_number:
        print "Your guess is too low, try again."
        return False
    elif guess == secret_number:
        # total_score = calculate_score()
        print "range_diff:", range_diff
        print "count:", count
        print "divide:", count/range_diff
        save_scores.append(count/float(range_diff))
        print "save scores: ", save_scores
        print "Well done, {}! You found my number in {} tries!".format(name, count)
        if min(save_scores) == count/float(range_diff):
            print "You are currently the winner with the best score!"
        ask_to_play_again()
        return True



def ask_to_play_again():
    answer = raw_input("Would you like to play again? Y/N: ")
    if answer == "Y" or answer == "y":
        number_guessing_game()
    elif answer == "N" or answer == "n":
        print "OK, bye!"
        return None
    else:
        print "I'm sorry, I didn't quite catch that. Please enter Y or N: "
        ask_to_play_again()


number_guessing_game()