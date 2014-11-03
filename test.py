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
	output = StringIO()

	app.run(10, output)
	i = 1
	for line in output.getvalue().splitlines():
	    self.failIf(i %% 3 = 0 and line != "Fizz")
	 

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
