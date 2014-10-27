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

    # Run from 2 to "end + 1". Version 2 functionality
    # 1 is not a prime number!
    def run(self, end, out=sys.stdout):
        for i in range(2, end + 1):
            for j in range(2, i):
                if i % j == 0:
                    break;
            else:
                print >> out, self.calc(i), "Is prime!"

    # Seems to give correct values. Tested with 1 and 2.
    def calc(self, i):
        return i

if __name__ == "__main__":
    app = FizzBuzz()
    app.run(100)
