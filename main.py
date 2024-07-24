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


def main():
    # import user records
    records = import_details(FILENAME)
    menu_choice = input(MENU_OPTIONS).lower()

    while menu_choice != 'q':
        if menu_choice == 'g':
            add_user(records)
        elif menu_choice == 'c':

            validate_password(records)
        # the following is only for when i break the code
        # elif menu_choice == 'f':
        #     salt = salt_password()
        #     hashed_password = hash_password("abCD##33", salt)
        #     fix_password("Lucas", hashed_password, salt)
        menu_choice = input(MENU_OPTIONS).lower()

    export_password(records)


def add_user(records):
    """Add a user to the current records."""
    username = input("input username: ")
    print(REQUIREMENTS)
    valid_password = input("< ")
    while not is_valid_password(valid_password):
        print('Invalid Password!\n', REQUIREMENTS)
        valid_password = input("Please enter a password: ")
    salt = salt_password()
    valid_password = hash_password(valid_password, salt)
    new_user = {"username": username, "password": valid_password, "salt": salt}
    records.append(new_user)


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


def salt_password():
    """Salt the password with a randomly generated key."""
    salt = ''.join([chr(int(random.uniform(33, 126))) for _ in range(16)])
    return salt


def hash_password(password, salt):
    """Hash the password with the generated salt."""
    salted_password = salt + password
    hash_object = hashlib.sha256(salted_password.encode())
    hashed_password = hash_object.hexdigest()
    return hashed_password


def export_password(records):
    """Save all records to json file."""
    save_details = []
    with open("password.json", "w", encoding="UTF-8") as out_file:
        for record in records:
            key_to_details = {"username": record['username'], "password": record['password'], "salt": record['salt']}
            save_details.append(key_to_details)
        json.dump(save_details, out_file)


def validate_password(records):
    username = input("Enter username: ")

    """Checks if a username is valid, and if the entered password matches the user record."""
    for record in records:

        if record['username'] == username:
            password = input("Enter password: ")
            test_hash = hash_password(password, record['salt'])
            if record['password'] == test_hash:
                print("Success!")
            else:
                print("Failure!")


def import_details(filename):
    """Load in records from a json file."""
    try:
        with open(filename, "r", encoding="UTF-8") as in_file:
            records = json.load(in_file)
    except FileNotFoundError:
        print(f"File {filename} not found")
        records = list()
    return records


def fix_password(username, password, salt):
    """ONLY FOR WHEN I BREAK THE JSON FILE"""
    save_details = []
    with open("password.json", "w", encoding="UTF-8") as out_file:
        key_to_details = {"username": username, "password": password, "salt": salt}
        save_details.append(key_to_details)
        json.dump(save_details, out_file)


def caeser_cipher(phrase, offset):
    # for i in range(len(phrase)):
    #     letter = phrase[i]
    #
    #     encrypted_phrase = "".join(chr((ord(letter) + offset) % 26))
    #
    # print(encrypted_phrase)
    #

    ans = ""
    # iterate over the given text
    for i in range(len(phrase)):
        ch = phrase[i]

        # check if space is there then simply add space
        if ch == " ":
            ans += " "
        # check if a character is uppercase then encrypt it accordingly
        elif ch.isupper():
            ans += chr((ord(ch) + offset - 65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly

        else:
            ans += chr((ord(ch) + offset - 97) % 26 + 97)

    return ans

    # # key = 'b'
    # key = get_random_bytes(8)
    #
    # cipher = DES.new(key, DES.MODE_ECB)
    #
    # phrase = b'Hello world'
    # padded_phrase = pad(phrase, DES.block_size)
    # encrypted_phrase = cipher.encrypt(padded_phrase)
    # # message = cipher.iv + cipher.encrypt(phrase)
    # print(encrypted_phrase)


main()
# caeser_cipher("hello", 2    )
