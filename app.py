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

    # Run from 1 to "end". Maybe. Test fails for some reason
    def run(self, end, out=sys.stdout):
        for i in range(1, end+1):
            print >> out, self.calc(i)

    # Seems to give correct values. Tested with 1 and 2.
    def calc(self, i):
<<<<<<< HEAD
        if i % 3 == 0 and i % 5 == 0:
=======
	if self.calcPrime(i) == 1:
	    return "%d is a prime" % i
        elif i % 3 == 0 and i % 5 == 0:
>>>>>>> prime
	    return "FizzBuzz"
	elif i % 3 == 0:
	    return "Fizz"
    	elif i % 5 == 0:
	    return "Buzz"
        else:
            return i
<<<<<<< HEAD
=======

    # Prime number calculation
    # Return 1 if prime number
    # Return 0 if not prime number
    def calcPrime(self, i):
	match = 0
	for val in range(1, i+1):
	    if i % val == 0:
		match += 1
	if match == 2:
	    return 1
        else:
	    return 0
>>>>>>> prime

if __name__ == "__main__":
    app = FizzBuzz()
    app.run(100)
