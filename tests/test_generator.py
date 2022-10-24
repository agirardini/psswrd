"""Tests for the generator module"""


import string
import unittest

from ..src.modules import generators


class TestGeneratorMethods(unittest.TestCase):

    def assertPassword(self, password, length, mode):
        """Custom assertion to test password constraints"""

        if mode == "numerical":
            characters_set = string.digits
        elif mode == "alphabetical":
            characters_set = string.ascii_letters
        elif mode == "alphanumerical":
            characters_set = string.ascii_letters + string.digits
        else:
            characters_set = string.ascii_letters + string.digits + string.punctuation

        if len(password) != length:
            self.fail("WRONG password length !!!")

        for char in password:
            if char not in characters_set:
                self.fail("WRONG characters set !!!")

    def test_generate_password(self):
        """Test generate_password function"""

        length = 30

        with self.subTest():
            password = generators.generate_password(length, "random")
            self.assertPassword(password, length, "random")

        with self.subTest():
            password = generators.generate_password(length, "numerical")
            self.assertPassword(password, length, "numerical")

        with self.subTest():
            password = generators.generate_password(length, "alphabetical")
            self.assertPassword(password, length, "alphabetical")

        with self.subTest():
            password = generators.generate_password(length, "alphanumerical")
            self.assertPassword(password, length, "alphanumerical")


if __name__ == '__main__':
    unittest.main()
