"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
def main():
    sum=0

    for i in range(1000000):
        currnumstr = str(i)
        binary = bin(i)[2:]
        if currnumstr==currnumstr[::-1] and binary == binary[::-1]:
            sum+=i
    
    print(sum)

if __name__ == '__main__':
    main()