"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
import math
from Problem35 import sieveOfErat

def listDivisors(n: int) -> list:
    """returns the list of distinct divisors of n"""
    ret = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i==0:
            if i not in ret:
                ret.append(i)
            if n/i != i and (n/i not in ret):
                ret.append(int(n/i))
    
    return sorted(ret)

def listPrimeDivisors(n: int) -> list:
    """returns the list of distinct prime divisors of n"""
    alldivs = listDivisors(n) #get all divisors
    maxnum = max(alldivs)
    listprimes = sieveOfErat(maxnum) #get the true list of primes until the highest #
    
    ret = []
    primesindex = 0
    divsindex = 0

    while (primesindex < len(listprimes)) and (divsindex < len(alldivs)):
        if listprimes[primesindex] < alldivs[divsindex]: #move primes pointer up
            primesindex += 1
        elif listprimes[primesindex] > alldivs[divsindex]: #move divs pointer up
            divsindex += 1
        else: #the elements are equal, move both elements up
            ret.append(alldivs[divsindex])
            divsindex += 1
            primesindex += 1

    return ret

def main():
    #print(listDivisors(644))
    #print(listPrimeDivisors(644))
    
    arr = [1,2,3,4]
    while(True):
        #print(arr)
        boolarr = [len(listPrimeDivisors(i))==4 for i in arr]
        if all(boolarr): #all 4 are consecutives that have 4 prime divisors
            print("ans: ",arr[0])
            break

        arr = [i+1 for i in arr]

if __name__ == '__main__':
    main()