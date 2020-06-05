public class Problem2
{
    public static void main(String[] args)
    {
        //By considering the terms in the Fibonacci sequence whose values do not exceed four million
        //find the sum of the even-valued terms.
        int sum = 0;
        int prev=1;
        int curr=2;

        while(curr <= 4000000)
        {
            //System.out.println("prev: " + prev + "\tcurr: " + curr);
            if (curr%2==0) //if even add to sum
                sum+=curr;

            int temp = prev;
            prev = curr; //move prev upwards
            curr += temp; //have the current num be itself + the previous
        }

        System.out.println(sum);
    }
}
