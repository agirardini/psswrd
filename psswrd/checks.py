"""This module implements all the functions necessary to check for password strength and commonness"""

import os

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
    """Check if password is included in a table of common password"""
    tables = {
        "1M": os.path.normpath("../data/common1M.txt"),
        "10k": os.path.normpath("../data/common10k.txt"),
        "100k": os.path.normpath("../data/common100k.txt"),
    }

    if table in tables.keys():
        with open(tables[table], "rt") as file:
            passwords = file.read().splitlines()

        if password in passwords:
            badnews = f"\n⚠️  ➜  I would {terminal_modifiers['RED']}{terminal_modifiers['BOLD']}NOT USE{terminal_modifiers['RESET']} this one bro, it's quite common.\n"
            print(badnews)
        else:
            goodnews = f"\n👻 ➜  You lucky bastard, you're password seems {terminal_modifiers['GREEN']}{terminal_modifiers['BOLD']}ORIGINAL{terminal_modifiers['RESET']}.\n"
            print(goodnews)


def check_strength(password):
    bad_password = f""
    good_password = f""
    fair_password = f""
    return
