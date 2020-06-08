"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import math
from Problem21 import d #d(n) gives you the sum of proper divisors of a number

def is_perfect(n: int) -> bool:
    return d(n) == n

def is_deficient(n: int) -> bool:
    return d(n) < n

perfectlist = list()
abundantlist = list()
def is_abundant(n: int) -> bool:
    """for i in perfectlist: #found off of wikipedia
        if n%i==0:
            return True
    
    for i in abundantlist: #another thing found off of wikipedia
        if n%i==0:
            return True"""
    
    return d(n) > n

def init_perfectlist():
    for i in range(2,28123):
        if is_perfect(i):
            perfectlist.append(i)

def init_abundantlist():
    for i in range(2,28123):
        if d(i) > i:
            abundantlist.append(i)

def main():
    total=0
    #init_perfectlist() #working ok
    #print(perfectlist)
    init_abundantlist() #working ok
    print(abundantlist)
    
    for num in range(1,28124):
        #need to see if num is a sum of abundant numbers
        is_sum = False
        for i in range(1,num+1):
            if (i in abundantlist) and (num-i in abundantlist):
                is_sum = True
                break
        
        if not(is_sum):
            total += num
    
    print(total)

if __name__ == '__main__':
    main()