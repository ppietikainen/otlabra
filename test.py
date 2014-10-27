import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != 1)
    
    def test_five(self):
        app = FizzBuzz()
        self.failIf(app.calc(5) != "5 is a prime")
        
    def test_seven(self):
        app = FizzBuzz()
        self.failIf(app.calc(7) != "7 is a prime")
    
    def test_ten(self):
        app = FizzBuzz()
        self.failIf(app.calc(10) != 10)
        
    def test_eighteen(self):
        app = FizzBuzz()
        self.failIf(app.calc(18) != 18)
    
    def test_fourtyfive(self):
        app = FizzBuzz()
        self.failIf(app.calc(45) != 45)
    
    def test_fortynine(self):
        app = FizzBuzz()
        self.failIf(app.calc(49) != 49)
    
    def test_fiftythree(self):
        app = FizzBuzz()
        self.failIf(app.calc(53) != "53 is a prime")
            
    def test_sixtyone(self):
        app = FizzBuzz()
        self.failIf(app.calc(61) != "61 is a prime")


    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
