"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from Problem35 import sieveOfErat #returns the list of primes from 2..upper using sieve of erat

def main():
    upper = 1000000
    lstprimes = sieveOfErat(upper)

    ans = 0
    for num in lstprimes:
        if num in (2,3,5,7): #problem restriction
            continue
        currstr = str(num)
        
        allareprime = True #flag
        #left to right
        for i in range(len(currstr)):
            currnum = int(currstr[i:])
            if currnum not in lstprimes: #if curr truncation is not prime, break
                allareprime = False
                break
        
        if not(allareprime): #break at this pt, no need for right to left
            continue

        #right to left
        for i in range(len(currstr)-1,-1,-1): #backwards from last char to first char
            currnum = int(currstr[:i+1])
            if currnum not in lstprimes:
                allareprime = False
                break
        
        if allareprime:
            ans+=num
    
    print(ans)

if __name__ == '__main__':
    main()