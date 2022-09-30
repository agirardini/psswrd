#! python

import checks
import generator
import argsparser

if __name__ == "__main__":

    # Arguments
    # length mode separator delimiter dictionary checktable checkstrength
    args = (argsparser.parse())
    # print(args)

    # password = None
    # password = "aerughpXPIUAC{I"
    password = "brady"

    # if args.mode == "random":
    #     password = generator.random_password()
    # elif args.mode == "numerical":
    #     password = generator.numerical_password()
    # elif args.mode == "alphabetical":
    #     password = generator.alphabetical_password()
    # elif args.mode == "passphrase":
    #     password = generator.passphrase()
    # else:
    #     pass

    if args["checktable"]:
        checks.check_table(password, args["checktable"])

    # if args.checkstrength:
    #     checks.check_strength()
