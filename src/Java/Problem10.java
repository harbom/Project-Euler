package Java;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
 */
public class Problem10
{
    private static List<Integer> primesUntil2Mil = new ArrayList<Integer>();

    public static void main(String[] args)
    {
        //use the sieve of erat to knock out all other composites and then sum over the primes
        sieveOfErat(2000000);

        //iterate over prime list and sum it up

        Long sum = 0L;
        for (int i:primesUntil2Mil)
        {

            sum+=i;
        }

        System.out.println(sum);
    }

    //builds a boolean array of indices 0..i. 1 will mean its a composite, 0 is that its prime
    public static void sieveOfErat(int i)
    {
        boolean[] table = new boolean[i+1];

        for (int index = 2; index < i; index++) //2 is the first prime
        {
            if (table[index] == true) //if it was marked as composite before, skip it
                continue;

            //if its gotten this far, its a prime
            primesUntil2Mil.add(index);

            //mark all multiples of current prime as composite aka assign a 1 to it
            for (int j = 2*index; j < i; j+=index)
            {
                table[j]=true; //assign every one but the current prime as composite
            }
        }

    }
}
