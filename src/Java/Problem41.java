/*
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
 */
package Java;

public class Problem41
{
    public static void main(String[] args)
    {
        long upperlimit = (long)Math.pow(10,9);

        //wakk back from the upper limit to reduce run time, print the first you see
        for (long i = upperlimit-2; i > 10; i--)
        {
            //optimizations to make runtime easier
            String currstring = String.valueOf(i);
            if (currstring.contains("0") || i%2==0) continue;

            if (!isStringPandigital(currstring,currstring.length())) continue;

            //System.out.println(i);
            if (isPrimeImproved(i))
            {
                System.out.println(i);
                break;
            }
        }
    }

    public static boolean isPrimeImproved(long num)
    {
        //only factors should be 1, num. no factors should be in [2,sqrt(num)]
        for (long i = 2; i < (int)Math.sqrt(num); i++)
            if (num%i==0) return false;

        return true;
    }

    public static boolean isStringPandigital(String num, int n)
    {
        if (num.length() != n) return false;

        for (int i = 1; i <= n; i++)
            if (getCount(num,i) != 1) return false;

        return true;
    }

    //returns the number of times target appears in string s
    public static int getCount(String s, int target)
    {
        int ct = 0;
        for (int i = 0; i < s.length(); i++)
            if (Integer.parseInt(s.substring(i,i+1)) == target)
                ct++;
        return ct;
    }
}
