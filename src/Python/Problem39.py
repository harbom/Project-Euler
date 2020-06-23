"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

def isPythagorean(a:int,b:int,c:int) -> bool:
    if not(c>b>a) or (a==b or b==c or a==c):
        return False
    return a**2 + b**2 == c**2

def main():
    #properties of triangle side lengths: triangle inequality
    #triple for loop? key word, RIGHT ANGLE TRIANGLE
    #if its a right angle triangle, the sides are pythagorean, and the three sides are unique/n3>n2>n1

    maxsols = 0
    for p in range(3,1001):
        currcount=0
        for n3 in range(int(p/2)+1,0,-1):
            for n2 in range(n3-1,0,-1):
                for n1 in range(n2-1,0,-1):
                    if isPythagorean(n1,n2,n3) and n1+n2+n3==p:
                        currcount+=1
        
        if currcount > maxsols:
            maxsols = currcount
    
    print(maxsols)

if __name__ == "__main__":
    main()