def main():
    ali = 21                          # Ali's age is given as 21 years old
    ahmed = ali + 6                   # Ahmed is 6 years older than Ali
    saqlain = ahmed + 20             # Saqlain is 20 years older than Ahmed
    bilal = saqlain + ali            # Bilal is as old as Saqlain's age plus Ali's age
    hamza = saqlain                  # Hamza is the same age as Saqlain

    # Print out all of the ages!
    print("Ali is " + str(ali))
    print("Ahmed is " + str(ahmed))
    print("Saqlain is " + str(saqlain))
    print("Bilal is " + str(bilal))
    print("Hamza is " + str(hamza))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
