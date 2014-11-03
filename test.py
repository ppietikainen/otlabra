import unittest
import sys
try:
    from StringIO import StringIO
else:
    from io import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != 1)
	
    def test_divisible_by_three(self):
    	app = FizzBuzz()
	self.failIf(app.calc(6) != "Fizz")
	
    def test_divisible_by_five(self):
        app = FizzBuzz()
	self.failIf(app.calc(10) != "Buzz")
	
    def test_divisible_by_both(self):
        app = FizzBuzz()
	self.failIf(app.calc(15) != "FizzBuzz")
	
    def test_correct_number_of_fizz(self):
        output = StringIO()
	
	app = FizzBuzz()
	app.run(10, output)
	
	self.failIf(output.getvalue().splitlines().count("Fizz") != 2)

    def test_correct_number_of_buzz(self):
        output = StringIO()
	
	app = FizzBuzz()
	app.run(20, output)
	
	self.failIf(output.getvalue().splitlines().count("Buzz") != 2)
	
    def test_correct_number_of_fizzbuzz(self):
        output = StringIO()
	
	app = FizzBuzz()
	app.run(40, output)
	
	self.failIf(output.getvalue().splitlines().count("FizzBuzz") != 2)

    def test_prime_one(self):
        app = FizzBuzz()
	self.failIf(app.isPrime(5) == False)

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
