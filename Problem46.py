"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from src.Python.Problem27 import isPrimeNaive
from src.Python.Problem35 import sieveOfErat

def main():
    currnum = 33

    while(True): #keep on going until something is found
        if isPrimeNaive(currnum):
            currnum += 2
            continue

        print("currnum: ",currnum)
        primelist = sieveOfErat(currnum) #get list of primes until that #
        #print("primelist: ",primelist)
        flag = False

        for currprime in primelist[::-1]: #go from highest to lowest to possibly reduce time
            currsum = currprime
            difference = int((currnum - currsum) / 2) #liberal guess based on pattern, allows space to guess for the squared term

            bigbreak = False
            for i in range(difference+5): #+5 just because why not lol
                if currsum + 2 * (i**2) == currnum: #its not the answer, we know this so avoid further reps
                    flag = True
                    bigbreak = True
                    print("Can be written: %d + 2*%d^2" % (currprime,i))
                    break
            
            if bigbreak:
                break

        print()

        
        #if not(flag) --> never found a pair of prime + 2*(square)
        if not(flag):
            print("ans: ",currnum)
            break
        else:
            currnum += 2
            


if __name__ == "__main__":
    main()