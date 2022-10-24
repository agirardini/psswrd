"""The 'argsparser' module implements argument parsing.

Classes:
    CustomParser(argparse.ArgumentParser):
        A wrapper of ArgumentParser for custom help message.

Functions:
    parse():
        Parse program's arguments.
"""


import os
import sys
import argparse


class CustomParser(argparse.ArgumentParser):
    """Wrapper of ArgumentParser for custom help message.

    This class is used to override 'print_help' and 'print_usage' standard behaviour in order to print a personalized help message contained in 'HELP_MESSAGE'.
    """

    HELP_MESSAGE = '''
usage: psswrd.py [-h] [-l LENGTH] [-n NUMBER] [-m {random, numerical, alphabetical, alphanumerical passphrase}] [-s SEPARATOR] [-d DELIMITER] [-D DICTIONARY] [-c {False, 10k, 100k, 1M}] [-C CHECKSTRENGTH]

A simple and handy password generator

options:
  -h, --help
                Print this beautiful help message

  -s, --separator SEPARATOR
                Set a separator

  -d, --delimiter DELIMITER
                Set a delimiter

  -D, --dictionary DICTIONARY
                Provide a dictionary

  -a, --acronym
                Make passphrase follow an acronym

  -l, --length LENGTH
                Set password length (default = 20)

  -n, --number NUMBER
                Generate 'number' passwords (default = 1)

  -w, --words WORDS
                Set number of 'words' to use for passphrase (default = 4)

  -S, --checkstrength
                Enable password strength checks (default = False)

  -C, --capitalized
                Make passphrase words capitalized (default = False)

  -c, --checktable {False, 10k, 100k, 1M}
                Enable checks on tables of common passwords (default = False)

  -m, --mode {random, numerical, alphabetical, alphanumerical, passphrase}
                Choose password type (default = random)

'''

    def print_help(self, file=None):
        if file is None:
            file = sys.stdout
        file.write(CustomParser.HELP_MESSAGE)

    def print_usage(self, file=None):
        if file is None:
            file = sys.stdout
        file.write(CustomParser.HELP_MESSAGE)


def parse():
    """
    Parse program's arguments.

    Returns:
        A dictionary of parsed arguments in the format {"ARG": "VALUE", ...}.
    """

    parser = CustomParser(
        description='A simple but handy password generator')

    parser.add_argument("-l", "--length",
                        type=int,
                        default=20,
                        dest="length",
                        choices=range(1, 100),
                        help="Set password length")

    parser.add_argument("-n", "--number",
                        type=int,
                        default=1,
                        dest="number",
                        help="Generate 'number' passwords")

    parser.add_argument("-s", "--separator",
                        type=str,
                        default=" ",
                        dest="separator",
                        help="Set a separator")

    parser.add_argument("-d", "--delimiter",
                        type=str,
                        default="",
                        dest="delimiter",
                        help="Set a delimiter")

    parser.add_argument("-w", "--words",
                        type=int,
                        default=4,
                        dest="words",
                        choices=range(2, 50),
                        help="Select number of words for passphrase")

    parser.add_argument("-D", "--dictionary",
                        type=str,
                        dest="dictionary",
                        default=os.path.normpath("../data/dictionary.txt"),
                        help="Provide a dictionary")

    parser.add_argument("-m", "--mode",
                        type=str,
                        dest="mode",
                        default="random",
                        choices=[
                            "random", "numerical", "alphabetical", "alphanumerical", "passphrase"], help="Choose password type")

    parser.add_argument("-S", "--checkstrength",
                        default=False,
                        action='store_true',
                        dest="checkstrength",
                        help="Enable password strength checks")

    parser.add_argument("-c", "--checktable",
                        type=str,
                        default="",
                        dest="checktable",
                        choices=["", "10k", "100k", "1M"],
                        help="Enable checks on tables of common passwords")

    parser.add_argument("-C", "--capitalized",
                        default=False,
                        dest="capitalized",
                        action='store_true',
                        help="Make passphrase words capitalized")

    parser.add_argument("-a", "--acronym",
                        type=str,
                        default="",
                        dest="acronym",
                        help="Make passphrase follow an acronym")


    return vars(parser.parse_args())

if __name__ == "__main__":
    print(parse())
