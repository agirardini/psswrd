"""This module implements all the password generator functions"""


import string
import secrets


def generate_password(length, mode):

    if mode == "numerical":
        characters_set = string.digits
    elif mode == "alphabetical":
        characters_set = string.ascii_letters
    elif mode == "alphanumerical":
        characters_set = string.ascii_letters + string.digits
    else:
        characters_set = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters_set) for i in range(length))
    return password


def generate_passphrase(length, separator, delimiter, dictionary):
    return
