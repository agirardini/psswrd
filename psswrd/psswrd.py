import checks
import generator
import argsparser

if __name__ == "__main__":

    args = (argsparser.parse())

    password = ""

    # if args["mode"] == "passphrase":
    #     password = generator.passphrase(
    #         args["length"], args["separator"], args["delimiter"], args["dictionary"])
    # else:
    #     password = generator.generate_password(args["length"], args["mode"])

    if args["checktable"]:
        checks.check_table(password, args["checktable"])

    if args["checkstrength"]:
        checks.check_strength(password)

    print()
    for i in range(10):
        print(generator.generate_password(
            args["length"], args["mode"]))
    print()
