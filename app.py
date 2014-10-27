#!/usr/bin/python
import sys

# Implementation of FizzBuzz v0.00

# Version 1: if number is divisible by 3, print Fizz
#            if number is divisible by 5, print Buzz
#            if both, print FizzBuzz
#            else print number

# Version 2: if number is prime, print "<number> is a prime" instead
#            Take one argument,  and count up to it

def isPrime(num):
    if(num != 1):
        a = num - 1
        while(a > 1):
            if(num % a == 0):
                return False
            a -= 1
        return True
    else:
        return False

class FizzBuzz():
    def __init__(self):
        pass

    # Run from 1 to "end". Maybe. Test fails for some reason
    def run(self, end, out=sys.stdout):
        for i in range(1, end + 1):
            print >> out, self.calc(i)

    # Seems to give correct values. Tested with 1 and 2.
    def calc(self, i):
        if(isPrime(i)):
            return ("%d is a prime" %i)
        else:
            return i

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        app = FizzBuzz()
        app.run(int(sys.argv[1]))
    else:
        print "Too few or many arguments given"
