import random

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print("Congratulations! You guessed the number.")
