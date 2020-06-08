"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

import math
def d(n) -> int:
    #summing all the divisors

    #only need to go up to sqrt(n) to check divisors
    divsum=0
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i==0:
            divsum += i #add both divisor and quotient
            if (n/i != n and n/i != i): #avoids case of like 2 being counted as a divisor for 4 twice
                divsum += n/i
    #print("n: ",n,"   divsum: ",divsum)
    
    return divsum

def main():
    bigtotal=0
    previous = set()
    for a in range(2,10000):
        if (a in previous and d(a) in previous):
            continue

        b = d(a)
        if (d(b)==a and a!=b): #and d(a)==b, its all good, a!=b for the condition of 'amicable' #s
            bigtotal += a + b
            previous.add(a)
            previous.add(b)

    print(bigtotal)

if __name__ == '__main__':
    main()