"""This module implements all the functions necessary to check for password strength and commonness"""


import os
import re


terminal_modifiers = {
    "BOLD": '\033[1m',
    "RED": '\033[91m',
    "RESET": '\033[0m',
    "BLUE": '\033[94m',
    "CYAN": '\033[96m',
    "GREEN": '\033[92m',
    "YELLOW": '\033[93m',
}


def check_table(password, table):
    """Check if password is included in a table of common password and print an adequate message"""
    tables = {
        "1M": os.path.normpath("../data/common1M.txt"),
        "10k": os.path.normpath("../data/common10k.txt"),
        "100k": os.path.normpath("../data/common100k.txt"),
    }

    if table in tables.keys():
        with open(tables[table], "rt") as file:
            passwords = file.read().splitlines()

        if password in passwords:
            badnews = f"\n⛔  ➜  I would {terminal_modifiers['RED']}{terminal_modifiers['BOLD']}NOT USE{terminal_modifiers['RESET']} this one bro, it's quite common.\n"
            print(badnews)
        else:
            goodnews = f"\n👻 ➜  You lucky bastard, you're password seems {terminal_modifiers['GREEN']}{terminal_modifiers['BOLD']}ORIGINAL{terminal_modifiers['RESET']}.\n"
            print(goodnews)


def check_strength(password):
    """Check password strength and print a coherent message"""

    if check_policies(password, 25, 3, 3, 3, 3):
        strong_password = f"\n🟢 ➜  Go on champ 💪🏼 this is a really {terminal_modifiers['GREEN']}{terminal_modifiers['BOLD']}STRONG{terminal_modifiers['RESET']} password.\n"
        print(strong_password)
        return

    if check_policies(password, 12, 2, 2, 2, 2):
        reasonable_password = f"\n🔵 ➜  This password is actually {terminal_modifiers['CYAN']}{terminal_modifiers['BOLD']}FINE{terminal_modifiers['RESET']} 🙃.\n"
        print(reasonable_password)
        return

    if check_policies(password, 8, 1, 1, 1, 1):
        weak_password = f"\n🟡 ➜  Meh... you can do way better, this one is pretty {terminal_modifiers['YELLOW']}{terminal_modifiers['BOLD']}WEAK{terminal_modifiers['RESET']} 🤕.\n"
        print(weak_password)
        return

    bad_password = f"\n🔴 ➜  No way, do not even try. This is {terminal_modifiers['RED']}{terminal_modifiers['BOLD']}SHIT{terminal_modifiers['RESET']} 💩.\n"
    print(bad_password)


def check_policies(password, length, digits, lowercase, uppercase, symbols):
    """Check if the string 'password' satisfies certain characters constraints

    'digits', 'lowercase', 'uppercase' and 'symbols' are all the number of corresponding characters that need to be present in 'password' to pass the check, given that 'length' is also fine
    """

    length_constraint = len(password) >= length
    digits_constraint = len(re.findall(r"\d", password)) >= digits
    lowercase_constraint = len(re.findall(r"[a-z]", password)) >= lowercase
    uppercase_constraint = len(re.findall(r"[A-Z]", password)) >= uppercase
    symbols_constraint = len(re.findall(
        r"[~!@#$%^&*()_+-={}\[\]|':;?/<>,." + r'"]', password)) >= symbols

    check = length_constraint and digits_constraint and lowercase_constraint and uppercase_constraint and symbols_constraint

    return check
