# psswrd
A simple and handy password generator

```
psswrd.py [-h] [-l LENGTH] [-m {random, numerical, alphabetical, alphanumerical, passphrase}] [-s SEPARATOR] [-d DELIMITER] [-D DICTIONARY] [-c {False, 10k, 100k, 1M}] [-C CHECKSTRENGTH]
```

OPTIONS:

> -h, --help

Print a beautiful help message

> -l, --length LENGTH

Set password length (default = 30)

> -m, --mode {random, numerical, alphabetical, alphanumerical, passphrase}

Choose password type (default = random)

> -s, --separator SEPARATOR

Set a separator

> -d, --delimiter DELIMITER

Set a delimiter

> -D, --dictionary DICTIONARY

Provide a dictionary

> -c, --checktable {"", 10k, 100k, 1M}

Enable checks on tables of common passwords (default = "")

> -C, --checkstrength

Enable password strength checks (default = False)
