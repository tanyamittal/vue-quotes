import java.util.Scanner;
class Box
{
    double length;
    double breadth;
    double height;
    void input()
    {
        Scanner sc = new Scanner (System.in);
        System.out.print("Enter dimensions:");
        length = sc.nextDouble();
        breadth = sc.nextDouble();
        height = sc.nextDouble();
    }
    void volume()
    {
        double vol = length*breadth*height;
        System.out.println("Volume of the box: "+vol);
    }
}
public class BoxDemo
{
    public static void main(String args[])
    {
        Box b = new Box();
        b.input();
        b.volume();
    }
}
