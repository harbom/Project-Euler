package Java;
/*
What is the value of the first triangle number to have over five hundred divisors?
 */
public class Problem12
{
    public static void main(String[] args)
    {
        //value for the n'th triangular number is sum(1..n) = n(n+1)/2

        int n = 1;
        long trisum = n*(n+1)/2L;

        while(numDivisorsNaive(trisum) <= 500)
        {
            //System.out.println(trisum);
            trisum = (++n)*(n+1)/2; //increment n and assign to trisum
        }

        System.out.println(trisum);
    }

    public static int numDivisorsNaive(long n)
    {
        int numdivisors=0;
        for (int i = 1; i <= Math.sqrt(n); i++) //only need to go up to sqrt(n) to check # divisors
        {
            if (n%i==0)
            {
                numdivisors+=2; //1 for i, 1 for n/i
            }
        }

        return numdivisors;
    }
}