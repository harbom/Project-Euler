"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from Problem38 import isStringPandigital
#from Problem35 import sieveOfErat
from Problem27 import isPrimeNaive

def main():
    #this method crashes, should prolly look for pandigitals first rather than primes as
    #there are less pandigitals than primes
    #lstPrimes = sieveOfErat(1000000000) #returns a list of primes up to 10**9, trims down computation

    upperlimit = 10**9

    #walk backwards from 10*9 to be more efficient, print the first one you see and terminate
    for i in range(upperlimit,9,-1):
        currstr = str(i)
        if isStringPandigital(str(i),len(str(i))):
            if isPrimeNaive(i):
                print(i)
                break

if __name__ == '__main__':
    main()