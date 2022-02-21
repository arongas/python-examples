import random

import hangman_art
import hangman_words

print(hangman_art.logo)

# Pick word and prepare
chosen_word = random.choice(hangman_words.word_list)
display = []
word_length = len(chosen_word)
for i in range(word_length):
    display += "_"

life = 6
while life > 0 and ("_" in display):
    print(display)
    # User choose letter
    guess = input("Please guess a letter: ").lower()
    idx = 0
    found = False
    for letter in chosen_word:
        if letter == guess:
            display[idx] = letter
            found = True
        idx += 1
    if not found:
        print(f"You guessed {guess}. That is not in the word, you loose life.")
        print(hangman_art.stages[life])
        life -= 1
    if  life > 0 and ("_" in display):
        print("Next Round")

if life == 0:
    print("You loose")
    print(hangman_art.stages[life])
else:
    print("You win")
