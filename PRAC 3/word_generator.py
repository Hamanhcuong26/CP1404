import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = "ccvcvvc"
word = ""

world_in = str(input("Please input your word: "))


def is_valid_format(world_in):
    for i in world_in:
        if i == 'c' or i == 'v':
            return True
        else:
            return False
            break

if is_valid_format(world_in):
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)