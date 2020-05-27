/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
 */

public class Problem7
{
    public static void main(String[] args)
    {
        //simple iteration, keep an array of 10001
        int index = 0;
        Long number = 2L;
        Long[] arr = new Long[10001];

        while (index != 10001) //index pointer isn't at the end of arr
        {
            if (Problem3.isPrimeNaive(number))
            {
                //System.out.println(number + " is prime at index " + index);
                arr[index] = number; //if its prime, set num in array and move the pointer
                index++;
            }

            number++; //incrememnt the number anyways
        }

        System.out.println(arr[10000]);
    }
}