"""This module implements all the password generator functions"""


import string
import secrets


def random_password(length):
    characters_set = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters_set) for i in range(length))
    return password


def numerical_password(length):
    characters_set = string.digits
    password = ''.join(secrets.choice(characters_set) for i in range(length))
    return password


def alphabetical_password(length):
    characters_set = string.ascii_letters
    password = ''.join(secrets.choice(characters_set) for i in range(length))
    return password


def passphrase(length, separator, delimiter, dictionary):
    return
