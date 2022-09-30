import checks
import generator
import argsparser

if __name__ == "__main__":

    args = (argsparser.parse())

    password = ""

    # if args["mode"] == "random":
    #     password = generator.random_password()
    # elif args["mode"] == "numerical":
    #     password = generator.numerical_password()
    # elif args["mode"] == "alphabetical":
    #     password = generator.alphabetical_password()
    # elif args["mode"] == "passphrase":
    #     password = generator.passphrase()
    # else:
    #     pass

    if args["checktable"]:
        checks.check_table(password, args["checktable"])

    if args["checkstrength"]:
        checks.check_strength(password)
