"""This module implements password generator functions.

Methods:
    generate_password(length, number, mode):
        Generate a list of passwords composed by differnt characters sets.

    generate_passphrase(dictionary, number, words, separator, delimiter):
        Generate a list of passphrase.
"""


import sys
import string
import secrets


def generate_password(length, number, mode):
    """
    Generate a password composed by differnt characters sets.

    Args:
        length:
            Required password length.
        number:
            How many passwords to generate.
        mode:
            Characters set to use {random, numerical, alphabetical, alphanumerical}.

    Returns:
        A list containing the required number of passwords that satisfies the requirements of the arguments
    """

    if mode == "numerical":
        characters_set = string.digits
    elif mode == "alphabetical":
        characters_set = string.ascii_letters
    elif mode == "alphanumerical":
        characters_set = string.ascii_letters + string.digits
    else:
        characters_set = string.ascii_letters + string.digits + string.punctuation

    passwords = []

    for i in range(number):
        passwords.append(''.join(secrets.choice(characters_set) for i in range(length)))

    return passwords


def generate_passphrase(dictionary, number, words, separator, delimiter):
    """
    Generate a passphrase.

    Args:
        dictionary:
            The path of a user supplied dictionary of words.
        number:
            How many passphrases to generate.
        words:
            Number of words to include in the passphrase.
        separator:
            A separator to add between words.
        delimiter:
            A delimiter to add both at beginning and end of passphrase.

    Returns:
        A list containing the required number of passphrases that satisfies the requirements of the arguments.

    Raises:
        IOError: An error occurred accessing the dictionary.
    """

    try:
        with open(dictionary, "rt") as file:
            word_list = file.read().splitlines()
    except Exception as error:
        sys.exit(f"Something went wrong while searching for your dictionary: {error}\n")

    passphrase_list = []

    for i in range(number):

        counter = words
        words_list = []
        while counter > 0:
            words_list.append(secrets.choice(word_list))
            counter -= 1

        passphrase = f"{separator}".join(words_list)

        if delimiter != "":
            passphrase = f"{delimiter}{passphrase}{delimiter}"

        passphrase_list.append(passphrase)

    return passphrase_list
