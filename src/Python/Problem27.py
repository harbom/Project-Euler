"""
Euler discovered the remarkable quadratic formula: n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79
. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""
import math

def f(a:int,b:int, n:int) -> int:
    return n**2 + a*n + b

def isPrimeNaive(n: int) -> bool:
    if n<0:
        return False #negative numbers aren't prime, additional factor of -1

    for i in range(2,int(math.sqrt(n)+1)): #only factors should be 1 and n, not anything in [2,sqrt(n)]
        if n % i == 0:
            return False
    
    return True

def main():
    maxlen=0
    maxprod=0

    for a in range(-999,1000):
        for b in range(-1000,1001):
            currlen = 0
            n = 0
            while(isPrimeNaive(f(a,b,n))):
                currlen += 1
                n += 1
            
            if currlen > maxlen:
                maxlen = currlen
                maxprod = a*b
    
    print(maxprod)

if __name__ == '__main__':
    main()