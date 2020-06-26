"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
def isStringPandigital(num: str, n:int) -> bool:
    """Returns if a string num is pandigital for n digits. Ex, 2143 is pandigital for 4 digits."""
    if len(num) != n:
        return False
    
    for i in range(1,n+1):
        if num.count(str(i)) != 1:
            return False
    return True

def main():
    #try to do it with reasonable bounds
    ans = 0

    nrange = 5
    for n in range(2,nrange):

        numrange = 10000
        for num in range(numrange):
            currstr = ""

            for i in range(1,n+1):
                currstr += str(num*i)
            
            if isStringPandigital(currstr,9):
                if int(currstr) > ans:
                    ans = int(currstr)
    
    print(ans)
            


if __name__ == "__main__":
    main()