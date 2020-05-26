//Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

public class Problem6
{
    public static void main(String[] args)
    {
        //just brute force is not bad

        Long sumofsquares = 0L;
        Long squareofsum = 0L;
        for (int i = 0; i <= 100; i++)
        {
            sumofsquares += i * i;
            squareofsum += i;
        }

        squareofsum *= squareofsum; //square the sum of 1..100
        System.out.println(squareofsum - sumofsquares);
    }
}
