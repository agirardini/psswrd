"""This module implements all password generator functions"""


import string
import secrets


def generate_password(length, mode):
    """Generate a password long 'length' and composed by differnt characters sets depending on the value of 'mode':

    - 'numerical': digits only
    - 'alphabetical': upper and lowercase letters
    - 'alphanumerical': digits and letters
    - 'random': digits, letters, punctuation characters
    """

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
    """"""
    return
