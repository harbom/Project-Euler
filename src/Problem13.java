/*
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(numbers are in Problem13Data.txt
 */

import java.io.File;
import java.io.IOException;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class Problem13
{
    public static void main(String[] args) throws IOException
    {
        String[] nums = readData();
        //System.out.println(Arrays.toString(nums));

        BigInteger sum = new BigInteger("0");
        for (String i:nums)
            sum = sum.add(new BigInteger(i));

        System.out.println(sum.toString().substring(0,10)); //only need the first 10 digits
    }

    private static String[] readData() throws IOException
    {
        String fpath = "src/Problem13Data.txt";
        Scanner s = new Scanner(new File(fpath));
        String[] ret = new String[100];

        int i = 0;
        while(s.hasNextLine())
        {
            ret[i] = s.nextLine();
            i++;
        }

        return ret;
    }
}
