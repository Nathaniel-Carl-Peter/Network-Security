"""
Password Manager
Author: Lucas O Brian
Forked: Nathaniel Carl Peter

import modules


password length = random number between 8-20

valid characters = abc...z

for i in length password length
    generated password.append(valid characters [random choice 0 to length of valid characters])


print generated password




"""

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import json
import random
import hashlib

VALID_CHARACTERS = ('a b c d e f g h i j k l m n o p q r s t u v w x y z '
                    'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
SPECIAL_CHARACTERS = "! @ # $ % ^ & * ( ) _ - = + ` ~ , . / ' [ ] < > ? { } | : ;"
REQUIREMENTS = "Password must have a lower case, upper case letter, 1 number and a special character"
MINIMUM_LENGTH_OF_PASSWORD = 8
MAXIMUM_LENGTH_OF_PASSWORD = 20
MENU_OPTIONS = "Menu\n(G)enerate new user and password\n(C)heck user and password\n(Q)uit\n"
FILENAME = "password.json"


def import_database(filename):
    try:
        with open(filename, 'r') as in_file:
            data = json.load(in_file)
    except FileNotFoundError:
        print(f"File {filename} not found")
    return data


def main():
    # import user records
    database = import_database(FILENAME)
    menu_choice = input(MENU_OPTIONS).lower()
    while menu_choice != 'q':
        if menu_choice == 'g':
            print(REQUIREMENTS)
            user_name = input('Username: ').title()
            user_password = input('User password: ')
        else:
            print('Invalid input')
        menu_choice = input(MENU_OPTIONS).lower()
    print('Have a good day')




def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MINIMUM_LENGTH_OF_PASSWORD or len(password) > MAXIMUM_LENGTH_OF_PASSWORD:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1
        else:
            print(char)
            return False
    # if any of the 'normal' counts are zero, return False
    if count_upper == 0 or count_lower == 0 or count_digit == 0 or count_special == 0:
        return False

    # if we get here (without returning False), then the password must be valid
    return True

main()
# caeser_cipher("hello", 2    )
