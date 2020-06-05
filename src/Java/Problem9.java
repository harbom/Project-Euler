package Java;
/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a2 + b2 = c2

        For example, 32 + 42 = 9 + 16 = 25 = 52.

        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.
*/
public class Problem9
{
    public static void main(String[] args)
    {
        //one theory is that c < sum/2 -> c < 500
        for (int c = 500; c >= 1; c--)
        {
            for (int b = 499; b >= 1; b--)
            {
                for (int a = 498;a >= 1; a--)
                {
                    boolean isPyth = (a*a + b*b == c*c) && (c > b && b > a);
                    boolean sumTrue = a+b+c == 1000;
                    if (isPyth && sumTrue)
                    {
                        System.out.printf("a:%d b:%d c:%d sum: %d\n",a,b,c,a*b*c);
                        break;
                    }
                }
            }
        }
    }
}
