from psswrd import checks


def report(passwords, checktable, checkstrength):
    """"""

    info = dict.fromkeys(passwords, ["", ""])

    if checktable:
        info = checks.check_table(info, checktable)

    if checkstrength:
        info = checks.check_strength(info)

    print_passwords(info)


def print_passwords(info):
    """"""

    print()
    counter = 1
    bold = checks.terminal_modifiers["BOLD"]
    reset = checks.terminal_modifiers["RESET"]
    for pswd, msg in info.items():
        print(f"{counter}. {bold}{pswd}{reset}")
        if msg[1]:
            print(f"{msg[1]}")
        if msg[0]:
            print(f"{msg[0]}")
        print()
        counter += 1
    print()
