#Find the sum of the digits in the number 100!
def factorial(n):
    ret = 1
    while(n>0):
        ret*=n
        n-=1
    return ret

print(sum(int(i) for i in str(factorial(100))))