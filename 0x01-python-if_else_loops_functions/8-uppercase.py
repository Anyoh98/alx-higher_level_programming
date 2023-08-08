#!/usr/bin/python3
def uppercase(str):
    result = ""
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            character = ord(character) - 32
        result += chr(character)
    print("{}".format(result))
