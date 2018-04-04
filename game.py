"""A number-guessing game."""
import random


save_scores = []
def number_guessing_game():
    print "Hi! Welcome to the Guessing Game!!"
    name = raw_input("What is your name? ")
    low, high = get_range()
    range_diff = high - low
    print "Low:", low, "High:", high
    secret_number = random.randint(low, high)
    print "Secret number: ", secret_number
    guess = 0
    count = 0
    while(guess != secret_number):
        guess = raw_input("Your guess? ")
        try:
            guess = int(guess)
            if guess in range (low, high+1):
                print "low: ", low, "high+1: ", high+1
                count += 1
                give_hints(guess, secret_number, name, count, range_diff)
            else:
                print "Oops! Valid numbers are integers between {}-{}. Please guess again within the integer range.".format(low, high)
        except:
            print "Oops! Please enter a valid integer in range {}-{}.".format(low, high)
            
def get_range():
    range = raw_input("The default range is 1-100. Press enter to accept or enter a custom range: ") or "1-100"
    try:
        result = tuple(map( lambda x: int(x), range.split('-') ))
        if result [0] == result[1]:
            print "Oops! That is not a valid range. Please try again."
            get_range()
        else:
            return result
    except:
        print "Oops! That is not a valid range. Please try again."
        get_range()

def give_hints(guess, secret_number, name, count, range_diff):
    if guess > secret_number:
        print "Your guess is too high, try again."
    elif guess < secret_number:
        print "Your guess is too low, try again."
    else:
        total_score = calculate_score()
        print "range_diff:", range_diff
        print "count:", count
        print "divide:", count/range_diff
        save_scores.append(count/float(range_diff))
        print "save scores: ", save_scores
        print "Well done, {}! You found my number in {} tries!".format(name, count)
        if min(save_scores) == count/float(range_diff):
            print "You are currently the winner with the best score!"
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

    

