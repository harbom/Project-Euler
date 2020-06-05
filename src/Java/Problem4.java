import java.util.*;

public class Problem4
{
    public static void main(String[] args)
    {
        /*
        A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

        Find the largest palindrome made from the product of two 3-digit numbers.
         */

        //do two for loops from 999 to 100, add each i*j into a list and return the largest in the list

        List<Integer> list = new ArrayList();
        for (int i = 999; i >= 100; i--)
            for (int j = 999; j >= 100; j--)
                if (!list.contains(i*j) && isPalindrome(i*j))
                    list.add(i*j);

        //find max of list by sorting and returning last val
        Collections.sort(list);
        System.out.println(list.get(list.size()-1));
    }

    private static boolean isPalindrome(int i)
    {
        StringBuilder s = new StringBuilder();
        s.append(i);

        return s.toString().equals(s.reverse().toString());
    }
}
