"""The 'presentation' module implements the functions necessary to report final results.

Functions:
    report(passwords, checktable, checkstrength):
        Gather additional info on the generated passwords (if required) and print results.
    print_results(info):
        Print to stdout the information contained in 'info'.
"""


from modules import checks


def report(passwords, args):
    """
    Gather additional info on the generated passwords (if required) and print results.

    Args:
        passwords:
            A list containing the generated passwords or passphrases.
        checktable:
            The value of the program argument CHECKTABLE which can be only one between "", "10k", "100k", "1M".
        checkstrength:
            The value of the program argument CHECKSTRENGTH which is a boolean.
    """

    info = dict.fromkeys(passwords, ["", ""])

    if args["checktable"]:
        info = checks.check_table(info, args["checktable"])

    if args["checkstrength"]:
        if args["mode"] == "passphrase":
            info = checks.check_passphrases_strength(info)
        else:
            info = checks.check_passwords_strength(info)

    print_results(info)


def print_results(info):
    """
    Print to stdout the information contained in 'info'.

    Args:
        info:
            A data structure of the format {"password": [checktable, checkstrength]}, where 'checktable' and 'checkstrength' are string messages relative to 'password'.
    """

    print()
    counter = 1
    bold = checks.terminal_modifiers["BOLD"]
    reset = checks.terminal_modifiers["RESET"]
    for pswd, msg in info.items():
        print(f"{counter}. {bold}{pswd}{reset}")
        if msg[1]:
            print(f"{msg[1]}")
        if msg[0]:
            print(f"{msg[0]}\n")
        print()
        counter += 1
    print()
