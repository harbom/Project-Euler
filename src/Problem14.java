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
    private static int currLength = 0;
    private static Map<Integer,Integer> numsToLengthMapping = new HashMap<Integer,Integer>();
    public static void main(String[] args)
    {
        int maxlen=0;
        int maxnum=0;

        //iterate regularly and update current highest length/numbers, return number at end
        for (int i = 1; i <= 20; i++)
        {
            int currlen = collatzChainLen(i);
            if (currlen > maxlen)
            {
                maxlen = currlen;
                maxnum=i;
            }
        }

        printMap();

        System.out.println(maxnum);
    }

    private static int collatzChainLen(int number)
    {
        int len = 1;
        int tempnum = number;
        if (tempnum ==1) return 1;
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

    //returns length of collatz chain for a given integer
    //doesnt seem to be working well, stack overflow issues
    private static void collatzChainLenRecursive(int number,int length)
    {
        if(number==1)
        {
            currLength = length; //+1 for the 1 in the sequence, store it in a class variable
            return;
        }

        //recurse
        else if (number%2==0)
        {
            collatzChainLenRecursive(number/2,length+1);
        }
        else
        {
            collatzChainLenRecursive(3*number +1,length+1);
        }
    }

    private static void printMap()
    {
        for (Map.Entry<Integer,Integer> i:numsToLengthMapping.entrySet())
        {
            System.out.printf("key: %d\tvalue: %d\n",i.getKey(),i.getValue());
        }
    }
}
