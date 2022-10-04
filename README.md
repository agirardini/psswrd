# psswrd
A handy password and passphrase generator

```
usage: psswrd.py [OPTIONS]

OPTIONS:

-h, --help
    Print a beautiful help message

-d, --delimiter DELIMITER
    Set a delimiter

-s, --separator SEPARATOR
    Set a separator

-D, --dictionary DICTIONARY
    Provide a dictionary

-l, --length LENGTH
    Set password length (default = 20)

-n, --number NUMBER
    Generate 'number' passwords (default = 1)

-w, --words WORDS
    Set number of 'words' to use for passphrase (default = 4)

-C, --checkstrength
    Enable password strength checks (default = False)

-c, --checktable {"", 10k, 100k, 1M}
    Enable checks on tables of common passwords (default = "")

-m, --mode {random, numerical, alphabetical, alphanumerical, passphrase}
    Choose password type (default = random)
```
