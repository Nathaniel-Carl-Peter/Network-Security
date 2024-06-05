"""
import modules


password length = random number between 8-20

valid characters = abc...z

for i in length password length
    generated password.append(valid characters [random choice 0 to length of valid characters])


print generated password




"""

import random
import hashlib

VALID_CHARACTERS = ('a b c d e f g h i j k l m n o p q r s t u v w x y z '
                    'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')

SPECIAL_CHARACTERS = "! @ # $ % ^ & * ( ) _ - = + ` ~ , . / ' [ ] < > ? { } |"

REQUIREMENTS = "Password must have a lower case, upper case letter, 1 number and a special character"

# length_of_password = random.randint(8, 20)
MINIMUM_LENGTH_OF_PASSWORD = 8
MAXIMUM_LENGTH_OF_PASSWORD = 20


def main():
    # valid_characters = VALID_CHARACTERS.split()
    # special_characters = SPECIAL_CHARACTERS.split()
    print(REQUIREMENTS)
    valid_password = input("< ")
    while not is_valid_password(valid_password):
        # password = []
        #
        # count += 1
        # for i in range(length_of_password):
        #
        #     character_choice = random.randint(0, 2)
        #     if character_choice == 0:
        #         password.append(valid_characters[random.randint(0, len(valid_characters) - 1)])
        #     elif character_choice == 1:
        #         password.append(special_characters[random.randint(0, len(special_characters) - 1)])
        #     else:
        #         password.append(str(random.randint(0, 9)))
        #     print(password)
        # valid_password = ''.join(password)
        print('Invalid Password!\n', REQUIREMENTS)
        valid_password = input("Please enter a password: ")
    print(valid_password)
    export_password(valid_password)


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
            return False
    # if any of the 'normal' counts are zero, return False
    if count_upper == 0 or count_lower == 0 or count_digit == 0 or count_special == 0:
        return False

    # if we get here (without returning False), then the password must be valid
    return True

def salt_password(password):
    salt_number = random.uniform()

    print()



def export_password(password):
    with open("password.txt", "w") as out_file:
        print(password, file=out_file)


main()
