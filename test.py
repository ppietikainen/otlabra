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
        app.run(1000, output)
        print output.getvalue().splitlines()

        self.failIf(len(output.getvalue().splitlines()) != 168)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
