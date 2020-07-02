package Java;
import java.util.*;

public class Problem47
{
    public static void main(String[] args)
    {
        //methods work well
        //System.out.println(listDivisors(644));
        //System.out.println(listPrimeDivisors(644));

        int[] arr = {20,21,22,23};
        while(true)
        {
            boolean flag = false;
            for (int i = 0; i < 4; i++)
            {
                //check each one individually and if any are false, break: no need to do further calculations
                boolean curr = listPrimeDivisors(arr[i]).size() == 4;
                if (!curr)
                {
                    flag = true;
                    break;
                }
            }

            //iterate on to the next
            if (flag)
            {
                for (int i = 0; i < 4; i++)
                    arr[i] += 1;

                continue;
            }

            //if it got here, it never had to break so all 4 entries are good
            System.out.println("answer: " + arr[0]);
            break;
        }
    }

    public static List<Integer> listDivisors(int n)
    {
        List<Integer> ret = new ArrayList<Integer>();
        for (int i = 1; i < (int)(Math.sqrt(n)+1); i++)
        {
            if (n%i==0) //if its a factor
            {
                if (!ret.contains(i)) //and not already in the ret list
                    ret.add(i);
                if (n/i != i && (!ret.contains(n/i))) //same but for the other factor
                    ret.add(n/i);
            }
        }

        Collections.sort(ret); //sort to aid in the 2 pointer method in listPrimeDivisors
        return ret;
    }

    public static List<Integer> listPrimeDivisors(int n)
    {
        List<Integer> alldivs = listDivisors(n);
        int maxnum = alldivs.get(alldivs.size()-1);
        List<Integer> listprimes = Problem35.sieveOfErat(maxnum); //efficient way for large #s

        List<Integer> ret = new ArrayList<Integer>();
        //Use 2 pointer method to do in O(N+M) instead of O(NM), relies off the fact that both are sorted arrays
        int primesindex = 0;
        int divsindex = 0;

        int primessize = listprimes.size();
        int divssize = alldivs.size();

        while(primesindex < primessize && divsindex < divssize)
        {
            if (listprimes.get(primesindex) < alldivs.get(divsindex)) //move prime pointer up
                primesindex++;
            else if (listprimes.get(primesindex) > alldivs.get(divsindex)) //move divs pointer up
                divsindex++;
            else //they are equal, add to the returned list
            {
                ret.add(alldivs.get(divsindex));
                divsindex++;
                primesindex++;
            }
        }

        return ret;
    }
}
