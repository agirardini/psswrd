import os


import os

from modules import generators
from modules import argsparser
from modules import presentation

def main():

    wd = os.path.dirname(os.path.realpath(__file__))
    os.chdir(wd)

    args = (argsparser.parse())

    passwords = []

    if args["mode"] == "passphrase":
        passwords = generators.generate_passphrase(args["dictionary"], args["number"], args["words"], args["separator"], args["delimiter"])
    else:
        for i in range(args["number"]):
            passwords = generators.generate_password(
                args["length"], args["number"], args["mode"])

    presentation.report(passwords, args)


if __name__ == "__main__":
    main()
