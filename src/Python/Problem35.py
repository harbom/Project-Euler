"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def sieveOfErat(upperlimit: int) -> list:
    primes = list()
    booltable = [True for i in range(upperlimit + 1)]

    for i in range(2,upperlimit):
        if booltable[i] == False: #you know its a composite
            continue

        #if its gotten this far, its a prime
        primes.append(i)

        #mark all multiples or current primes until upperlimit as composite
        for j in range(2*i,upperlimit,i): #step by i
            booltable[j] = False
    
    return primes

def main():
    #can first do the sieve of erat to narrow down the candidates
    upperlimit=1000000
    listprimes = sieveOfErat(upperlimit)
    numcircprimes = 0

    for num in listprimes:
        currstr = str(num)
        currlen = len(currstr)
        
        
        areRotationsPrimeList = list()
        for i in range(currlen):
            #197, 971, 719: 197 is original string so its str[i:] + str[:i] to find all rotations
            currrotation = currstr[i:] + currstr[:i]
            
            areRotationsPrimeList.append(int(currrotation) in listprimes) #boolean
        
        if all(areRotationsPrimeList):
            numcircprimes += 1
    
    print(numcircprimes)
    


if __name__ == '__main__':
    main()