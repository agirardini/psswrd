# psswrd
A simple and handy password generator

```
psswrd.py [-h] [-l LENGTH] [-n NUMBER] [-m {random, numerical, alphabetical, alphanumerical, passphrase}] [-s SEPARATOR] [-d DELIMITER] [-D DICTIONARY] [-c {False, 10k, 100k, 1M}] [-C CHECKSTRENGTH]
```

OPTIONS:

> -h, --help

Print a beautiful help message

> -d, --delimiter DELIMITER

Set a delimiter

> -s, --separator SEPARATOR

Set a separator

> -D, --dictionary DICTIONARY

Provide a dictionary

> -l, --length LENGTH

Set password length (default = 30)

> -n, --number NUMBER

Generate 'number' passwords (default = 1)

> -C, --checkstrength

Enable password strength checks (default = False)

> -c, --checktable {"", 10k, 100k, 1M}

Enable checks on tables of common passwords (default = "")

> -m, --mode {random, numerical, alphabetical, alphanumerical, passphrase}

Choose password type (default = random)
