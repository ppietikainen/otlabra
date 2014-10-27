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
        lines = output.getvalue().splitlines()
        self.failIf(len(output.getvalue().splitlines()) != 100)
        self.failIf(lines[0] != "1")
        self.failIf(lines[99] != "Buzz")
        self.failIf(lines[30] != "<31> is a prime")

def main():
    unittest.main()

if __name__ == "__main__":
    main()
