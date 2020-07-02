"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def main():
    #try naive way
    val = 0
    for i in range(1,1001):
        val += i**i
    
    print(str(val)[-10:])

if __name__ == "__main__":
    main()