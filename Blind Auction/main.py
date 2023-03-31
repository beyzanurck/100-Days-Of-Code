import art
import os

print(art.logo)

print("Welcome to the secret auction program")

continue_checking = "y"
blind_participant = {}

def find_higgest_bidder(bidder_record):
    """
    Find the highest price and print the name
    """
    max_price = 0
    winner = ""

    for bidder in bidder_record:
        if bidder_record[bidder] > max_price:
            max_price = bidder_record[bidder]
            winner = bidder

    print(f"the winner is {winner} with ${max_price}")


while continue_checking == "y":

    name = input("What is your name? ")
    price = input("What is your price? $")

    blind_participant[name] = int(price)

    continue_checking = input("Is there any other participant? y/n\n")

    if continue_checking == "y":
        os.system('cls')
    else:
        find_higgest_bidder(blind_participant)
