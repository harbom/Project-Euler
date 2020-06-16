"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
def main():

    totalnumerator = 1
    totaldenominator = 1
    for numerator in range(10,100):
        for denominator in range(numerator+1,100): #fraction has to be < 1
            if numerator%10==0 or denominator%10==0:
                continue #trivial fraction?

            numstr = str(numerator)
            denomstr = str(denominator)

            #see if theres 1 and only 1 common num in both numstr and denomstr
            seen = set()
            for a in numstr:
                if a in denomstr:
                    seen.add(a)
            
            if len(seen) != 1: #case of 24/42, not in the case of 22/42. or, if the set is empty, nothing is common -> continue
                continue

            #splice the digit out
            commondigit = seen.pop()
            numindex,denomindex = numstr.index(commondigit), denomstr.index(commondigit)
            numstr,denomstr = numstr[:numindex] + numstr[numindex+1:],denomstr[:denomindex] + denomstr[denomindex+1:]


            #print("num: %s, den: %s, numstr: %s, denomstr: %s" % (numerator,denominator,numstr,denomstr))

            newfrac = int(numstr)/int(denomstr)
            #print("newfrac: ",newfrac)

            if newfrac == numerator/denominator:
                totalnumerator *= numerator
                totaldenominator *= denominator
    
    #print("final: %d/%d" % (totalnumerator,totaldenominator))

    #now we need to reduce it
    #both num and denom are divisible by gcd(num,denom), answer will be totalnum/gcd(num,denom) as gcd <= totalnum
    
    #divisors of num are atmax num, walk backwards from that
    import math
    gcd=totalnumerator
    while(not(totalnumerator%gcd==0 and totaldenominator%gcd==0)):
        gcd-=1
    
    print("answer: ", totaldenominator/gcd)

if __name__ == "__main__":
    main()