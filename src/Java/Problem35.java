/*
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
 */
package Java;
import java.util.*;

public class Problem35
{
    public static void main(String[] args)
    {
        int upperlimit = 1000000;
        List<Integer> listprimes = sieveOfErat(upperlimit);
        int numcircprimes = 0;

        for (int num:listprimes)
        {
            String currstr = String.valueOf(num);
            boolean areRotationsGood = true;

            int currlen = currstr.length();
            for (int i = 0; i < currlen; i++)
            {
                String currrotation = currstr.substring(i) + currstr.substring(0,i);

                if (!listprimes.contains(Integer.parseInt(currrotation)))
                {
                    areRotationsGood = false;
                    break;
                }
            }

            if (areRotationsGood)
                numcircprimes++;
        }

        System.out.println(numcircprimes);
    }

    public static List<Integer> sieveOfErat(int upperlimit)
    {
        List<Integer> primes = new ArrayList<Integer>();
        boolean[] booltable = new boolean[upperlimit+1];

        for (int i = 2; i < upperlimit; i++)
        {
            //its a composite
            if (booltable[i] == true) continue;

            //if its gotten this far its a prime
            primes.add(i);

            //mark all multiples of i as composites, step by i
            for (int j = i*2; j < upperlimit; j+=i)
            {
                booltable[j] = true;
            }
        }

        return primes;
    }
}
