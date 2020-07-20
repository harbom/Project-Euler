"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from Problem27 import isPrimeNaive

#look at problem24.java for permutation intuition
def permute(prefix,string,lst):
    n = len(string)
    if n==0:
        if prefix[0] == '0': #'invalid' #, won't really be a 4 digit number
            return
        elif int(prefix) in lst:
            return
        elif not(isPrimeNaive(int(prefix))):
            return

        lst.append(int(prefix))
    else:
        for i in range(len(string)):
            permute(prefix + string[i], string[0:i] + string[i+1:],lst)

def binarysearch(arr: list, target: int) -> int:
    """returns an index (may be -1) of the index of target in an array"""

    low = 0
    high = len(arr)-1

    while(low <= high):
        midindex = int((high+low)/2)
        if arr[midindex] == target:
            return midindex
        elif arr[midindex] < target: #go to right, after mid
            low = midindex + 1
        else: #go to left after mid
            high = midindex-1
    
    return -1

def main():
    for i in range(1000,10000):
        #each of the 3 numbers must be prime and must be permutations of the same base #
        perms = []
        permute("",str(i),perms) #currperms is now filled with the 
        perms = sorted(perms) #to form the 'arithmetic sequence'

        if len(perms) < 3: #further optimization
            continue
        
        #need to find every sublst with length 3
        #can optimize this by binary search: O(n) * O(lgn) * O(lgn) --> O(nlg^2(n)) -> O(nlgn)
        for j in range(len(perms)):
            curr = perms[j]
            first_target = 3330+curr
            first_index = binarysearch(perms,first_target)
            if first_index == -1: #not in array
                continue

            second_target = 3330 + first_target
            second_index = binarysearch(perms,second_target)
            if second_index == -1: #not in array
                continue
            else:
                #all 3 in the array
                print(curr,perms[first_index],perms[second_index])


if __name__ == "__main__":
    main()