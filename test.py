import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != (1, ""))

    def test_run(self):
        output = StringIO()

        # Test if the amount of fizzbuzzes is correct in range 1-20
        app = FizzBuzz()
        app.run(20, output)

        fizz_am = 5
        buzz_am = 3
        fizzbuzz_am = 1
        fizz_am_test = buzz_am_test = fizzbuzz_am_test = 0
        
        for line in output.getvalue().splitlines():
            if "FizzBuzz" in line:
                fizzbuzz_am_test += 1
            elif "Fizz" in line:
                fizz_am_test += 1
            elif "Buzz" in line:
                buzz_am_test += 1

        self.failIf(fizz_am_test != fizz_am or buzz_am_test != buzz_am \
            or fizzbuzz_am_test != fizzbuzz_am)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
