/*
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
 */
package Java;

public class Problem39
{
    public static void main(String[] args)
    {
        int maxsols = 0;
        int maxp = 0;

        for (int p = 10; p <= 1000; p++)
        {
            //System.out.println("currp: " + p);
            int currcount = 0;
            for (int c = p/2+1; c >= 1; c--)
            {
                for (int b = c-1; b >= 1 && b<c; b--)
                {
                    for (int a = b-1; a >= 1 && a<b; a--)
                    {
                        if (a*a + b*b == c*c && a+b+c==p)
                        {
                            currcount+=1;
                            //System.out.printf("a,b,c: %d%d%d\n",a,b,c);
                        }
                    }
                }
            }

            if (currcount > maxsols)
            {
                maxsols = currcount;
                maxp = p;
            }
            //System.out.println();
        }

        System.out.printf("maxsols: %d\t maxp: %d",maxsols,maxp);
    }
}
