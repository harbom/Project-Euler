"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def is_string_zero_to_n_pandigital(upper: int, s: str) -> bool:
    """Returns if a string num is pandigital for 0_n digits. Ex, 1023456789 is 0-to-n pandigital for 9 digits."""
    
    if len(s) != upper+1:
        return False
    
    for i in range(0,upper+1):
        if s.count(str(i)) != 1:
            return False
    return True

def follows_divisibility_rules(n: str) -> bool:
    """returns whether or not a string follows problem 42 divisibilty rules"""

    all_multiplications = [int(n[i] + n[i+1] + n[i+2]) for i in range(1,8)]
    check_arr = [2,3,5,7,11,13,17]

    for i in range(len(all_multiplications)):
        if all_multiplications[i] % check_arr[i] != 0:
            return False
    
    return True

def main():
    ans = 0

    
    for i in range(10**8,10**9):
        currstr = str(i)
        if not(is_string_zero_to_n_pandigital(9,currstr)):
            continue

        if follows_divisibility_rules(currstr):
            ans += i
    
    print(ans)



if __name__ == '__main__':
    main()