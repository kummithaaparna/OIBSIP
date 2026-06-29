import random
import string

while True:
    print("\n=== Random Password Generator ===")

    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password must be at least 8 characters long.")
            continue

        print("\nChoose character types:")
        upper = input("Include uppercase letters? (y/n): ").lower() == "y"
        lower = input("Include lowercase letters? (y/n): ").lower() == "y"
        numbers = input("Include numbers? (y/n): ").lower() == "y"
        symbols = input("Include symbols? (y/n): ").lower() == "y"

        characters = ""

        if upper:
            characters += string.ascii_uppercase
        if lower:
            characters += string.ascii_lowercase
        if numbers:
            characters += string.digits
        if symbols:
            characters += string.punctuation

        selected = sum([upper, lower, numbers, symbols])

        if selected < 2:
            print("Please select at least two character types.")
            continue

        password = "".join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (y/n): ").lower()
        if again != "y":
            print("Thank you for using the Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")