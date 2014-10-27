import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != (1, ""))

    def test_negative(self):
        app = FizzBuzz()
        self.failIf(app.calc(-1000) != (-1000, ""))

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(1000, output)

        prime_amount = 0

        for line in output.getvalue().splitlines():
            if "Is prime!" in line:
                prime_amount += 1

        self.failIf(prime_amount != 168)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
