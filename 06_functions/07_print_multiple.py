def print_multiple(message: str, repeats: int):
    for i in range(repeats):      # Repeat loop 'repeats' times
        print(message)            # Print the message each time


def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)


if __name__ == '__main__':
    main()
