"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import math
def main():
    """
    7x7 example just for visualization

    43 44 45 46 47 48 49
    42 21 22 23 24 25 26
    41 20 7  8  9  10 27
    40 19 6  1  2  11 28
    39 18 5  4  3  12 29
    38 17 16 15 14 13 30
    37 36 35 34 33 32 31
    """

    """
    for 5x5: (25 + 21 + 17 + 13) + (9 + 7 + 5 + 3) + (1)
                -4       -4     -4      -2    -2   -2     

    for 7x7: (49 + 43 + 37 + 31) + (25 + 21 + 17 + 13) + (9 + 7 + 5 + 3) + (1)
                 -6   -6   -6    -6    -4   -4   -4     -4   -2  -2  -2   -2  
    
    so start by taking n-1 away from n**2 4 times, then sub n-1 again and do n-3 4 times... until you get to 1
    """

    n = 1001
    subtract = n-1

    temp = n**2
    sum = 0
    for i in range(int(n/2)):
        for j in range(4): #for the 4 corners of the current square
            sum += temp
            #print("currtemp: %s, currsum: %s, subtract: %s" % (temp,sum,subtract))
            temp -= subtract
        
        subtract -= 2 #move on to the next 'square'

        #print("after round %d: currtemp: %s, currsum: %s, subtract: %s" % (i,temp,sum,subtract))
    
    sum += 1 #for the last inner bit

    print(sum)
    
if __name__ == "__main__":
    main()