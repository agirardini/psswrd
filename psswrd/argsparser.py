"""This module implements argument parsing"""

import sys
import argparse

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

  -l, --length LENGTH
                Set password length (default = 30)

  -n, --number NUMBER
                Generate 'number' passwords (default = 1)

  -C, --checkstrength
                Enable password strength checks (default = False)

  -c, --checktable {False, 10k, 100k, 1M}
                Enable checks on tables of common passwords (default = False)

  -m, --mode {random, numerical, alphabetical, alphanumerical, passphrase}
                Choose password type (default = random)

'''

class CustomParser(argparse.ArgumentParser):

    def print_help(self, file=None):
        if file is None:
            file = sys.stdout
        file.write(HELP_MESSAGE)

    def print_usage(self, file=None):
        if file is None:
                file = sys.stdout
        file.write(HELP_MESSAGE)

def parse():
    parser = CustomParser(
        description='A simple but handy password generator')

    parser.add_argument("-l", "--length",
                        type=int,
                        default=30,
                        help="Set password length")

    parser.add_argument("-n", "--number",
                        type=int,
                        default=1,
                        help="Generate 'number' passwords")

    parser.add_argument("-m", "--mode",
                        type=str,
                        default="random",
                        choices=[
                            "random", "numerical", "alphabetical", "alphanumerical", "passphrase"], help="Choose password type")

    parser.add_argument("-s", "--separator",
                        type=str,
                        default=None,
                        help="Set a separator")

    parser.add_argument("-d", "--delimiter",
                        type=str,
                        default=None,
                        help="Set a delimiter")

    parser.add_argument("-D", "--dictionary",
                        type=str,
                        default=None,
                        help="Provide a dictionary")

    parser.add_argument("-c", "--checktable",
                        type=str,
                        default="",
                        choices=["", "10k", "100k", "1M"],
                        help="Enable checks on tables of common passwords")

    parser.add_argument("-C", "--checkstrength",
                        default=False,
                        action='store_true',
                        help="Enable password strength checks")

    return vars(parser.parse_args())
