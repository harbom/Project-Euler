import java.util.ArrayList;

public class Problem3
{
    public static void main(String[] args)
    {
        /*
        The prime factors of 13195 are 5, 7, 13 and 29.

        What is the largest prime factor of the number 600851475143 ?
        */

        Long retvalue = 0L;
        Long n = 600851475143L;

        //cant cast a double to a long so im taking the string workaround
        String s = "" + Math.sqrt(n);
        s = s.substring(0,s.indexOf("."));
        Long sqrtn = Long.parseLong(s);

        //iterate down from n and return the first prime factor you encounter
        //prime factors of n are <= sqrt(n):   https://proofwiki.org/wiki/Composite_Number_has_Prime_Factor_not_Greater_Than_its_Square_Root
        for (Long i = sqrtn; i >= 1; i--)
        {
            if (n % i != 0) //avoids unnecessary calls to isPrime
                continue;

            if(isPrimeNaive(i))
            {
                retvalue = i;
                break;
            }
        }

        System.out.println(retvalue);

    }

    private static boolean isPrimeNaive(Long l)
    {
        //add all factors from 1..l into a list, check if list only has 2 elements: just 1 and l
        //factors of a number are <= n/2 (simple examples are like no greater factors of 100 than 50 etc)
        ArrayList<Long> factors = new ArrayList();
        for (Long i = 1L; i <= l/2; i++)
        {
            if (l % i == 0)
                factors.add(i);

            if (factors.size() > 1) //limits unnecessary looping
                return false;
        }

        return true; //hasn't returned false so it must be true
    }
}
