import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

def find_the_number(dificulty_level):
    remaining = 0 
    guessed_number = 0
    random_number = random.randint(1,100)

    while remaining < dificulty:
        guessed_number = int((input("Make a guess: ")))
        if guessed_number == random_number:
            print("You win !!!")
            remaining = dificulty
        else:
            remaining +=1

            if guessed_number < random_number:
                print("too low")
            else:
                print("too high")
            
            print(f"You have {dificulty - remaining} attempts reamining to guess the number.\n Guess again.")

dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ")

if dificulty == "easy":
    print("You have 10 attemp remaining to guess the number.")
    dificulty = 10
else:
    print("You have 5 attemp remaining to guess the number.")
    dificulty = 5


find_the_number(dificulty)    
