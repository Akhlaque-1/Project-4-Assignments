import random

words = ['apple', 'banana', 'cherry']
word = random.choice(words)
guessed = ['_'] * len(word)
tries = 6

while tries > 0 and '_' in guessed:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        tries -= 1
    print(' '.join(guessed))
    print(f"Tries left: {tries}")

if '_' not in guessed:
    print("You won!")
else:
    print(f"You lost! The word was {word}")
