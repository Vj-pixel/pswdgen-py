import math
import random
import string

def get_character_set(choice):
    char_sets = {
        '1': string.digits,
        '2': string.ascii_letters,
        '3': string.punctuation
    }

    choices = [c.strip() for c in choice.split(',')]

    if '4' in choices:
        print("You didn't follow the directions! :(")
        exit()

    return ''.join(char_sets.get(c, '') for c in choices)

def get_valid_password_length():
    while True:
        try:
            length = input("How many characters do you want in your password? ")
            length = int(length)
            if length <= 2:  # Check if password is too short
                print("Password must be at least 3 characters long for security!")
                continue
            if length <= 0:
                print("Please enter a positive number!")
                continue
            return length
        except ValueError:
            print("That's not a valid number! Please enter a positive integer.")

password_length = get_valid_password_length()

print('''Choose character set for password from these:
        1. Digits
        2. Letters
        3. Special characters
        4. Exit
        You can choose multiple btw!
        Say it like this: 1,3
        Don't say 4 in any of them though! You'll exit the program!
        DO NOT REPEAT NUMBERS FOR NO REASON!''')

while True:
    choice = input("Pick a number: ")
    character_list = get_character_set(choice)
    if character_list:
        break
    print("Invalid input! Please use numbers 1-3 separated by commas.")

if len(character_list) > 0:
    password = ''.join(random.choice(character_list) for _ in range(password_length))
    print(f"Your password is: {password}")
else:
    print("No valid character sets selected!")
