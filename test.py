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
	self.failIf(app.calc(6) != "Fizz")

    def test_five(self):
	app = FizzBuzz()
	self.failIf(app.calc(10) != "Buzz")

    def test_fifteen(self):
	app = FizzBuzz()
	self.failIf(app.calc(15) != "FizzBuzz")

    def test_prime(self):
	app = FizzBuzz()
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	for i in primes:
	    self.failIf(app.calc(i) != "%d is a prime" % i)

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

	fizz = 0
	buzz = 0
	fizzbuzz = 0

	for i in output.getvalue().splitlines():
	    if i.strip() == "Fizz":
		fizz += 1
	    elif i.strip() == "Buzz":
		buzz += 1
	    elif i.strip() == "FizzBuzz":
		fizzbuzz += 1

        self.failIf(len(output.getvalue().splitlines()) != 100)
	self.failIf(fizzbuzz != 6)
	self.failIf(fizz != 26)
	self.failIf(buzz != 13)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
