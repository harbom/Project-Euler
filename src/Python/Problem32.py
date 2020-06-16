"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def ispandigital(mult1: int,mult2: int, product: int) -> bool:
    string = "%d%d%d" % (mult1,mult2,product)
    if len(string) != 9: #9 digits only
        return False

    for i in range(1,10):
        if string.count(str(i)) != 1: #each val only appears once
            return False
    
    return True

def main():
    #brute force iteration

    seen = set() #to avoid double counting 
    for a in range(9999):
        for b in range(9999):
            prod = a*b
            if ispandigital(a,b,prod) and prod not in seen:
                #print("a: %d, b: %d, prod: %d" % (a,b,prod))
                seen.add(prod)
    
    print(sum(seen))

if __name__ == "__main__":
    main()