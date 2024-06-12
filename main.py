"""
import modules


password length = random number between 8-20

valid characters = abc...z

for i in length password length
    generated password.append(valid characters [random choice 0 to length of valid characters])


print generated password




"""
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


def main():
    # import user records
    records = import_details()
    menu_choice = input(MENU_OPTIONS).lower()

    while menu_choice != 'q':
        if menu_choice == 'g':
            add_user(records)
        elif menu_choice == 'c':
            check_username = input("Enter username: ")
            check_password = input("Enter password: ")
            validate_password(records, check_username, check_password)
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


def validate_password(records, username, password):
    """Checks if a username is valid, and if the entered password matches the user record."""
    for record in records:
        if record['username'] == username:
            test_hash = hash_password(password, record['salt'])
            if record['password'] == test_hash:
                print("Success!")
            else:
                print("Failure!")


def import_details():
    """Load in records from a json file."""
    with open("password.json", "r", encoding="UTF-8") as in_file:
        records = json.load(in_file)
    return records


def fix_password(username, password, salt):
    """ONLY FOR WHEN I BREAK THE JSON FILE"""
    save_details = []
    with open("password.json", "w", encoding="UTF-8") as out_file:
        key_to_details = {"username": username, "password": password, "salt": salt}
        save_details.append(key_to_details)
        json.dump(save_details, out_file)


main()
