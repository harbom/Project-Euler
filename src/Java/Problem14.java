package Java;
/*
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
 */

import java.util.*;

public class Problem14
{
    private static Map<Integer,Long> numsToLengthMapping = new HashMap<Integer,Long>();
    public static void main(String[] args)
    {
        long maxlen=0;
        long maxnum=0;

        //iterate regularly and update current highest length/numbers, return number at end
        for (int i = 1; i <= 999999; i+=2)
        {
            long currlen = collatzChainLen(i);
            if (currlen > maxlen)
            {
                maxlen = currlen;//currLength;
                maxnum=i;
            }
        }

        //printMap();

        System.out.println(maxnum);
    }

    private static long collatzChainLen(int number)
    {
        long len = 1;
        int tempnum = number;
        while(tempnum != 1)
        {
            if (numsToLengthMapping.containsKey(tempnum)) //deal with case of seeing past numbers
            {
                len = len + numsToLengthMapping.get(tempnum)-1; //-1 for the overlap of the current loop and the past loop?
                break;
            }

            if (tempnum%2==0)
                tempnum/=2;
            else
                tempnum = tempnum*3 + 1;
            len++;
        }


        //store it here for further use
        numsToLengthMapping.put(number,len);
        return len;
    }

    private static void printMap()
    {
        for (Map.Entry<Integer,Long> i:numsToLengthMapping.entrySet())
        {
            System.out.printf("key: %d\tvalue: %d\n",i.getKey(),i.getValue());
        }
    }
}

/*
    //returns length of collatz chain for a given integer
    //doesnt seem to be working well, stack overflow issues
    private static void collatzChainLenRecursive(int number,int tempnum, int length)
    {
        if(number==1)
        {
            currLength = length;
            numsToLengthMapping.put(number,length);
            return;
        }

        if (numsToLengthMapping.containsKey(tempnum)) //deal with case of seeing past numbers
        {
            currLength = length + numsToLengthMapping.get(tempnum)-1; //-1 for the overlap of the current loop and the past loop?
            return;
        }
        //recurse
        else if (tempnum%2==0)
        {
            collatzChainLenRecursive(number,tempnum/2,length+1);
        }
        else
        {
            collatzChainLenRecursive(number,3*tempnum +1,length+1);
        }
    }
*/
