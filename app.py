#!/usr/bin/python
import sys

# Implementation of FizzBuzz v0.00

# Version 1: if number is divisible by 3, print Fizz
#            if number is divisible by 5, print Buzz
#            if both, print FizzBuzz
#            else print number

# Version 2: if number is prime, print "<number> is a prime" instead
#            Take one argument,  and count up to it

class FizzBuzz():
    def __init__(self):
        pass

    # Run from 1 to "end + 1". Version 1 functionality.
    def run(self, end, out=sys.stdout):
        for i in range(1, end + 1):
            print >> out, self.calc(i)[0], self.calc(i)[1]

    # Test for a single value
    def calc(self, val):
        message = ""
        if val % 3 == 0 and val % 5 == 0:
            message = "FizzBuzz"
        elif val % 3 == 0:
            message = "Fizz"
        elif val % 5 == 0:
            message = "Buzz"
        return (val, message)

if __name__ == "__main__":
    app = FizzBuzz()
    app.run(100)
