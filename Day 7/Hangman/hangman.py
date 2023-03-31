import random
import hangman_art
import os

stages = hangman_art.stages #shapes of the hangman
logo = hangman_art.logo
print(logo)

from hangman_words import word_list
word_list = word_list

chosen_word = random.choice(word_list)

display = []
for i in range(len(chosen_word)):
  display.append("_")

lives = 6
end_of_the_game = False

while not end_of_the_game:  
  guess = input("\nGuess a letter: ").lower()

  os.system('cls')

  if guess in display:
    print("You already guessed it")

  for position in range(len(chosen_word)):
    if guess == chosen_word[position]:
      display[position] = guess

  if not guess in chosen_word:
    print(f"You guessed {guess}, that's not in the word. YOU LOSE A LIFE.")
    lives -=1
    
    hangman = stages.pop(lives)
    print(hangman)
    
    if lives == 0:
      end_of_the_game = True
      print(f"YOU LOSE.\nThe word is: {chosen_word}")
    
  print(f"\n{display}")

  if "_" not in display:
    end_of_the_game = True
    print("\nYOU WIN !!!")
