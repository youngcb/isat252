#test_fizzbuzz.py

#import the code to be tested 
from fizzbuzz import Fizzbuzz

# a smoke test
def test_smoke():
	assert True == True

def test_fizz():
	assert Fizzbuzz.fizz(3) == "fizz"

