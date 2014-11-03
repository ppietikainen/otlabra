import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != 1)

    def test_three(self):
        app = FizzBuzz()
        self.failIf(app.calc(9) != "Fizz")

    def test_both(self):
        app = FizzBuzz()
        self.failIf(app.calc(15) != "FizzBuzz")

    def test_division(self):
        app = FizzBuzz()
        self.failIf(app.calc(168) != "Fizz")

    def test_big(self):
        app = FizzBuzz()
        self.failIf(app.calc(700) != "Buzz")

    def test_big_both(self):
        app = FizzBuzz()
        self.failIf(app.calc(705) != "FizzBuzz")

    def prime_test_1(self):
        app = Primes()
        self.failIf(app.calc(11) != "11 is a prime")

    def prime_test_big(self):
        app = Primes()
        self.failIf(app.calc(5077) != "5077 is a prime")

    def prime_test_notaprime(self):
        app = Primes()
        self.failIf(app.calc(5076) == "5076 is a prime")

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
