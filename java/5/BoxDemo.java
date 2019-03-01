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
class Area extends Box
{
  void area()
  {
      double ar = 2 * (length*breadth + breadth*height + height * length);
      System.out.println("Area of the box: "+ar+"square units");
  }
}
public class BoxDemo
{
    public static void main(String args[])
    {
        Area b = new Area();
        b.input();
        b.volume();
        b.area();
    }
}
