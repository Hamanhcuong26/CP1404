"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def get_password(password):
    if len(password) > MIN_LENGTH & len(password) < MAX_LENGTH:
        print('The length of your password is valid.')
    else :
        print("NOT Valid!! Please enter a valid password")
        password = input("> ")

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for x in password:
        if x.islower():
            count_lower = count_lower + 1
        if x.isupper():
            count_upper = count_upper + 1
        if x.isdigit():
            count_digit = count_digit + 1
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    else:
        print('Characters are valid.')
    if SPECIAL_CHARS_REQUIRED:
        if x in SPECIAL_CHARACTERS:
            count_special = count_special + 1
        if count_special == 0:
            return False
        else:
            print('Special Requirements Characters are valid.')
    return True


print("Please enter a valid password")
print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
print("\t1 or more uppercase characters")
print("\t1 or more lowercase characters")
print("\t1 or more numbers")
password = input(">")
get_password(password)
if SPECIAL_CHARS_REQUIRED:
    print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not get_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),password))

