from psswrd import checks
from psswrd import generator
from psswrd import argsparser

if __name__ == "__main__":

    args = (argsparser.parse())
    # print(args)

    passwords = []

    if args["mode"] == "passphrase":
        for i in range(args["number"]):
            passwords.append(generator.passphrase(args["dictionary"]),
                args["length"], args["separator"], args["delimiter"], )
    else:
        for i in range(args["number"]):
            passwords.append(generator.generate_password(
                args["length"], args["mode"]))

    if args["checktable"]:
        checks.check_table(passwords, args["checktable"])

    if args["checkstrength"]:
        checks.check_strength(passwords)

    print()
    counter = 1
    for pswd in passwords:
        print(f"{counter}. {pswd}")
        counter += 1
    print()
