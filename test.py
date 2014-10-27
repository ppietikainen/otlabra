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
        
    def test_hardcore(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(10000, output)

        self.failIf(len(output.getvalue().splitlines()) != 10000)
        
    def test_primes(self):
        app = FizzBuzz()
        f = open('primes.txt', 'r')
        for line in f:
	        self.failIf(app.is_prime(int(line)) != True)

    def test_nonprimes(self):
        app = FizzBuzz()
        f = open('nonprimes.txt', 'r')
        for line in f:
	        self.failIf(app.is_prime(int(line)) != False)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
