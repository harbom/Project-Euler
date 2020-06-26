/*
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
 */
package Java;

import java.util.Arrays;

public class Problem43
{
    private static int[] checkArr = {2,3,5,7,11,13,17};

    public static void main(String[] args)
    {
        long ans = 0;

        for (long i = (long)Math.pow(10,9); i < (long)Math.pow(10,10); i++)
        {
            String currstr = String.valueOf(i);

            boolean flag = false;

            //check for pandigital-ness
            for (int j = 0; j <= 9; j++)
            {
                if (currstr.replace(""+j,"").length()  != 9)
                {
                    flag = true;
                    break;
                }
            }

            if (flag) continue;

            //if it got here its not false yet, can continue with same bool
            //check for the divisibility rules
            for (int j = 1; j <= 7; j++)
            {
                if (Integer.parseInt(currstr.substring(j,j+3)) % checkArr[j-1] != 0)
                {
                    flag = true;
                    break;
                }
            }

            //if it got here its good
            if (!flag)
            {
                System.out.println("LO: " + i);
                ans += i;
            }
        }

        System.out.println("answer: " + ans);
    }
}