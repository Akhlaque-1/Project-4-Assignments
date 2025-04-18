low = 1
high = 100
feedback = ''
print("Think of a number between 1 and 100.")

while feedback != 'c':
    guess = (low + high) // 2
    feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1

print(f"Yay! I guessed it: {guess}")
