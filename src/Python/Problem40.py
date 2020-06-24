"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def main():
    string = str()
    for i in range(1,1000001): #populate the string
        string += str(i)
    
    #get the answer
    ans = int(string[0])
    for i in range(1,7):
        ans *= int(string[int('9'*i)]) #so it goes string[9],string[99]...string[999999]
    print(ans)

if __name__ == "__main__":
    main()