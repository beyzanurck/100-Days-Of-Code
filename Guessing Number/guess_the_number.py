from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

def set_dificulty():
    level = input("Choose a dificulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)

    turns = set_dificulty()

    guess = 0
    while guess != answer:    

        print(f"You have {turns} attemp remaining to guess the number.")

        guess = int((input("Make a guess: ")))
        turns = check_answer(guess, answer, turns)
 
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was {answer}")
            return
        elif guess != answer:
            print("Guess again.")


game()
