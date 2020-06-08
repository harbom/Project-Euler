/*
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
 */
package Java;
import java.util.*;

public class Problem23
{
    private static Set abundantlist = new HashSet<Integer>();
    public static void main(String[] args)
    {
        init_abundantlist();

        int total=0;
        for (int num = 1; num <= 28123; num++)
        {
            boolean is_sum = false;
            for (int i = 2; i <= num; i++)
            {
                if (abundantlist.contains(i) && abundantlist.contains(num-i))
                {
                    is_sum = true;
                    break;
                }
            }

            if (!is_sum)
                total += num;
        }


        System.out.println(total);
    }

    private static void init_abundantlist()
    {
        for (int i = 2; i < 28124; i++)
        {
            if (sum_proper_divisors(i) > i)
            {
                abundantlist.add(i);
            }
        }
    }

    private static int sum_proper_divisors(int n)
    {
        int divsum=0;
        for (int i = 1; i < (int)(Math.sqrt(n)+1); i++)
        {
            if (n%i==0)
            {
                divsum += i;
                if (n/i != n && n/i != i)
                    divsum += n/i;
            }
        }

        return divsum;
    }
}
