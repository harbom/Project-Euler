package Java;
/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 */


public class Problem5
{
    public static void main(String[] args)
    {
        //2 loops is the trivial solution
        boolean isdiv = false;
        int number=20;
        while(!isdiv)
        {
            number++;
            for (int i = 1; i <= 20; i++)
            {
                if (number % i != 0)
                    break;

                //if it reached 20 and hasn't broke yet, the number passed all cases
                if (i==20) isdiv = true;
            }
        }

        System.out.println(number);
    }
}
