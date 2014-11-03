import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != 1)
    
    #test division by three
    def test_three_division(self):
	app = FizzBuzz()
	
	self.failIf(app.calc(3) != "Fizz")

    #test division by five
    def test_five_division(self):
        app = FizzBuzz()

        self.failIf(app.calc(5) != "Buzz")
	 
    #test division by three and five
    def test_three_and_five_division(self):
        app = FizzBuzz()
        output = StringIO()

        self.failIf(app.calc(15) != "FizzBuzz")


    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
