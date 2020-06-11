/*
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
 */

package Java;
import java.util.*;

public class Problem24
{
    private static List<String> permutations = new ArrayList<String>();
    private static int n = 3;
    private static String str = "0123456789";
    public static void main(String[] args)
    {
        //make a function to generate permutations of a string, preferably put them in an array
        //need to sort the array, then return the 999999'th element

        permute("",str); //start off with a blank prefix, full string
        System.out.println(permutations.size());
        Collections.sort(permutations);

        System.out.println(permutations.get(999999));
        /*for (String i:permutations)
        {
            System.out.println(i);
        }*/
    }

    private static void permute(String prefix, String str)
    {
        int n = str.length();
        if (n==0)
            permutations.add(prefix); //result is when the prefix has 10 letters and str has 0
        else
        {
            for (int i = 0; i < n; i++) //iterate over all indices of str
            {
                //new prefix will be the prefix until now with the current iterated character added on,
                //str will be what the string was before, besides that 1 character

                //so itll start from prefix="", str = "0123456789" to prefix = "0","1"... and str = "12345..","02..","013..." etc respectively
                permute(prefix + str.charAt(i),str.substring(0,i) + str.substring(i+1));

                //this guarantees that the length of str gets smaller and smaller with further recursive calls, adding the removed character to prefix

                //it guarantees all possible combos because if a call is prefix="0" and str="123456789", all/only letters from str will be added to prefix
            }
        }
    }
}
