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
	k = 0
        for i in range(2, end+1):
		for j in range(2, i):		
			if i % j == 0: 
				k = 1
		if k==0:
			print >> out, "%d is a prime" % i
		k = 0
    # Seems to give correct values. Tested with 1 and 2.
    def calc(self, i):
        return i

if __name__ == "__main__":
    nmb = int(sys.argv[1])
    app = FizzBuzz()
    app.run(nmb)
