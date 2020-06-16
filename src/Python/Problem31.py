"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

coins = [1,2,5,10,20,50,100,200]

def main():
    print(countRecursive(coins,8,200)) #start with all 8 coins, target of 200


def countRecursive(coins, numcoins, target):
    """
    can divide the problem into 1) sets with atleast 1 m coin and 2) sets with no mth coin

    solution will be the # of sets without S_m + the # of sets with atleast S_m
    """

    if target==0: #no money, we have our solution, add 1 to the bigger subproblem
        return 1
    
    if target<0: #negative money, disregard curr solution
        return 0
    
    if numcoins<=0 and target>=1: #we run out of coins, return 0
        return 0
    
    return countRecursive(coins,numcoins-1,target) + countRecursive(coins,numcoins,target-coins[numcoins-1])
    #  ^current problem      =   ^ sum using all but the m'th coin           ^sum using all coins without the mth coin
    #if a solution cointains S_m, we can use all the coins and solve for the target of target-S_m
    #if a solution does not contain S_m, you subtract 1 from numcoins 

if __name__ == "__main__":
    main()