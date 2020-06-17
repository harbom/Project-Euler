"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def factorial(n: int) -> int:
    if n==0:
        return 1
    
    ret=1
    while(n>=1):
        ret*=n
        n-=1
    
    return ret

def doesqualify(n: int) -> bool:
    factsum = 0
    for i in str(n):
        factsum += factorial(int(i))
    
    return factsum==n

def main():
    ans=0
    for i in range(10,999999):
        if doesqualify(i):
            ans += i
    
    print(ans)

if __name__ == '__main__':
    main()