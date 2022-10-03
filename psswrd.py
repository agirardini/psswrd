from psswrd import checks
from psswrd import generator
from psswrd import argsparser

def main():

    args = (argsparser.parse())

    passwords = []

    if args["mode"] == "passphrase":
        passwords = generator.generate_passphrase(args["dictionary"], args["number"], args["words"], args["separator"], args["delimiter"])
    else:
        for i in range(args["number"]):
            passwords = generator.generate_password(
                args["length"], args["number"], args["mode"])

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


if __name__ == "__main__":
    main()
