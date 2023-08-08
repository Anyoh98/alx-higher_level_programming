#!/usr/bin/python3
for lowercase in range(97, 123):
    if lowercase == 113 or lowercase == 101:
        continue
    print("{}".format(chr(lowercase)), end="")
