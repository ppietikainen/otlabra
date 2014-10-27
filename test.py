import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != 1)

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)

    def test_ver1(self):
        app = FizzBuzz()
        self.failIf(app.calc(87) != "Fizz")
        self.failIf(app.calc(20) != "Buzz")
        self.failIf(app.calc(45) != "FizzBuzz")
        self.failIf(app.calc(1500) != "FizzBuzz")
        self.failIf(app.calc(37284) != "Fizz")

def main():
    unittest.main()

if __name__ == "__main__":
    main()
