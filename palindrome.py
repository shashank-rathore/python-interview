#Write a Python program to check if a string is a palindrome.

import os
import sys

STRING=input("Enter a string: ")

REV_SRTING = STRING[::-1]

if STRING == REV_SRTING:
    print("Hurray! You have passed a palandrome string.")
else:
    print("You have passed a normal string. please try again!")


