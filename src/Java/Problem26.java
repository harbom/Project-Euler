/*
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
 */
package Java;
import java.math.BigInteger;

public class Problem26
{
    public static void main(String[] args)
    {
        /* 3 cases, help from https://medium.com/@aiswaryamathur/length-of-recurring-cycle-repetend-in-decimal-representation-of-a-unit-fraction-1afe6461cc59
            1) terminating decimals, like 1/2 or 1/4
                - 10^k*(1/n) -> is an integer => n is a factor of 10^k => n = 2^a * 5^b, with k being max(a,b)
                - If a number can be represented as (2^a)*(5^b), its reciprocal is a terminating decimal => don't have to worry about it
            2) decimals with repeating digits, like 1/3 or 1/7
                - 10^k*(1/n) - (1/n) is an integer => 10^k - 1 mod n = 0 => 10^k mod n = 1
                - so we need to find the least value of k for which 10^k mod n = 1
            3) decimals with digits repeating after the first digit, like 1/6
                - Once all multiples of 2 and 5 are cancelled out from n, it can be solved as Case 2 from above.
                - In other words, the non-repeating part of the decimal representation is contributed to by the 2’s and 5’s in n.
                - Since we are interested in the repeating cycle, we can factorize n, remove all multiples of ( 2 and 5) and solve it as for Case 2 above.
         */

        int maxlen=0;
        int num=0;
        int max = 1000;
        for (int n = 3; n < max; n++)
        {
            int factorized = factorize2and5Out(n);
            //System.out.println("num: " + n + "   factorized: " + factorized);

            if (factorized != 1) //if it == 1, its terminating so we're good
            {
                //here, we need to find the max length cycle of the repeating digits

                //need to find the least value of k for which 10^k mod n = 1, where k is the length of the repeating cycle
                //modular property: 10^2 mod n == 10*10 mod n == 10 mod n * 10 mod n


                //int k = getLength(factorized);
                int k = 1;
                String placeholder = "";
                placeholder += factorized;


                BigInteger tenexpo = BigInteger.TEN;
                BigInteger modBigInteger = new BigInteger(placeholder);

                while(!tenexpo.mod(modBigInteger).equals(BigInteger.ONE))
                {
                    k += 1;
                    tenexpo = tenexpo.multiply(BigInteger.TEN);
                }

                if (k > maxlen)
                {
                    maxlen = k;
                    num = n;
                }
            }
        }

        System.out.println(num);
    }

    private static int factorize2and5Out(int n)
    {
        while (n%2==0 || n%5==0)
        {
            if (n%2==0) n/=2;
            if (n%5==0) n/=5;
        }

        return n;
    }
}