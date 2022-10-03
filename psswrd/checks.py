"""This module implements the functions necessary to check for password strength and commonness

Functions:

"""


import os
import re
import sys


terminal_modifiers = {
    "BOLD": '\033[1m',
    "RED": '\033[91m',
    "RESET": '\033[0m',
    "BLUE": '\033[94m',
    "CYAN": '\033[96m',
    "GREEN": '\033[92m',
    "YELLOW": '\033[93m',
}


def check_table(passwords, table):
    """Check if password is included in a table of common password and print an adequate message"""

    tables = {
        "1M": os.path.normpath("./data/common1M.txt"),
        "10k": os.path.normpath("./data/common10k.txt"),
        "100k": os.path.normpath("./data/common100k.txt"),
    }

    if table in tables.keys():
        try:
            with open(tables[table], "rt") as file:
                common_passwords = file.read().splitlines()
        except Exception as error:
            sys.exit(f"Unable to retrieve the passwords table: {error}\n")

        badnews = f"⛔  ➜  I would {terminal_modifiers['RED']}{terminal_modifiers['BOLD']}NOT USE{terminal_modifiers['RESET']} this one bro, it's quite common."
        goodnews = f"👻 ➜  You lucky bastard, you're password seems {terminal_modifiers['GREEN']}{terminal_modifiers['BOLD']}ORIGINAL{terminal_modifiers['RESET']}."

        for pswd, msg in passwords.items():
            if pswd in common_passwords:
                passwords[pswd][0] = badnews
            else:
                passwords[pswd][0] = goodnews

    return passwords


def check_strength(passwords):
    """Check password strength and print a coherent message"""

    strong_password = f"🟢 ➜  Go on champ 💪🏼 this is a really {terminal_modifiers['GREEN']}{terminal_modifiers['BOLD']}STRONG{terminal_modifiers['RESET']} password."
    reasonable_password = f"🔵 ➜  This password is actually {terminal_modifiers['CYAN']}{terminal_modifiers['BOLD']}FINE{terminal_modifiers['RESET']} 🙃."
    weak_password = f"🟡 ➜  Meh... you can do way better, this one is pretty {terminal_modifiers['YELLOW']}{terminal_modifiers['BOLD']}WEAK{terminal_modifiers['RESET']} 🤕."
    bad_password = f"🔴 ➜  No way, do not even try. This is {terminal_modifiers['RED']}{terminal_modifiers['BOLD']}SHIT{terminal_modifiers['RESET']} 💩."

    for pswd, msg in passwords.items():

        if check_policies(pswd, 20, 3, 3, 3, 3):
            passwords[pswd][1] = strong_password
            continue
        if check_policies(pswd, 12, 2, 2, 2, 2):
            passwords[pswd][1] = reasonable_password
            continue
        if check_policies(pswd, 8, 1, 1, 1, 1):
            passwords[pswd][1] = weak_password
            continue
        else:
            passwords[pswd][1] = bad_password

    return passwords

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
