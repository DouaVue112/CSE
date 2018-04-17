""""
a general guide for hangman
1. Make a word  bank - 10 items
2. Pick an item from the list
3. Hide the word (use*)
4. Reveal letters already guessed
5. Create the win condition

"""
import random
import string
letters = list(string.ascii_lowercase)
Word_Bank = ["animal", "parents", "fight", "gaming", "playing", "volleyball", "soccer", "school", "animation", "fun"]
guess_left = 10
random_word = random.choice(Word_Bank)

letter_selected =[]
correct = list(random_word)

Guess = ""
while Guess != "Quite":
    output = []
    for letter in random_word:
        if letter in letter_selected:
            output.append(letter)
        else:
            output.append("*")
    print(" ".join(list(output)))

    if Guess not in random_word:
        guess_left -= 1
        print(guess_left)
    if output == correct:
        print ("You win")
        exit(0)
    if guess_left == 0:
        print("You lose")
        exit(0)

    Guess = input("Guess a letter:")
    print("These are your Letter %s" % letter_selected)

    lower = Guess.lower()
    letter_selected.append(lower)
