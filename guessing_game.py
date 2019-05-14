import random

lower_num = 1
higher_num = 10

def start_game():
    print("Welcome to the Number Guessing Game!")
    high_score = 0
    answer = random.randint(lower_num,higher_num) 
    #How to generate a random number in python (https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/)
    attempts = 0
    while True:
        
        try:
            user_guess = int(input("Pick a number between {} & {}: ".format(lower_num,higher_num)))
            if user_guess > higher_num:
                raise ValueError
            elif user_guess < lower_num:
                raise ValueError
        except ValueError as err:
            print("Oh no! That's not a valid number, please enter a number between {} and {}".format(lower_num,higher_num))
            continue
        else:
            attempts += 1
            if user_guess > answer:
                print ("It's lower")
                continue
            elif user_guess < answer:
                print ("It's higher")
                continue
            print("Got it! It took you {} attempt(s)".format(attempts))
            if high_score == 0:
                high_score = attempts
            elif high_score > attempts:
                high_score = attempts
            while True:
                try:
                    try_again = input("Would you like to play again? Enter y for yes or n for no!:   ")
                    if try_again.lower() not in ["n", "y"]:
                        raise ValueError
                except ValueError as err:
                    print("You can only enter y or n, please try again")
                    continue
                else:
                    break
            if try_again.lower() == "y":
                answer = random.randint(lower_num,higher_num)
                attempts = 0
                print("The current high score is {} attempt(s). Good luck beating it!".format(high_score))
                continue
            else:            
                print("Thank you for playing!")
                break


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
