import java.util.*;
import java.lang.System;
public class maxmin
{
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        int[] array= new int[10];
        System.out.println("Enter the numbers now");
        for(int i=0; i<10;i++)
        {
            int next = input.nextInt();
            array[i]=next;
        }
        System.out.println("These are the no you have entered");
        printArray(array);
        int a = getmaxvalue(array);
        int w = getminvalue(array);
        System.out.println("\nMax value is :"+a);
        System.out.println("Min value is :"+w);
    }

    public static int getmaxvalue(int array[])
    {
        int maxvalue = array[0];
        for(int i =1;i<10;i++)
        {
            if(array[i]>maxvalue)
                maxvalue=array[i];
        }
        return maxvalue;
    }
    public static int getminvalue(int array[])
    {
        int minvalue = array[0];
        for(int i =1;i<10;i++)
        {
            if(array[i]<minvalue)
                minvalue=array[i];
        }
        return minvalue;
    }
    public static void printArray(int array[])
    {
        int n = array.length;
        for (int i = 0;i<n;i++)
        {
            System.out.print(array[i]+" ");
        }
    }
}
