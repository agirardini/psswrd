from psswrd import generator
from psswrd import argsparser
from psswrd import presentation

def main():

    args = (argsparser.parse())

    passwords = []

    if args["mode"] == "passphrase":
        passwords = generator.generate_passphrase(args["dictionary"], args["number"], args["words"], args["separator"], args["delimiter"])
    else:
        for i in range(args["number"]):
            passwords = generator.generate_password(
                args["length"], args["number"], args["mode"])

    presentation.report(passwords, args["checktable"], args["checkstrength"])


if __name__ == "__main__":
    main()
