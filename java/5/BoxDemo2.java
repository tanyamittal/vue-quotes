import static java.lang.System.out;
import java.util.Scanner;
class Box
{
    double length;
    double breadth;
    double height;
    void input()
    {
        Scanner sc = new Scanner (System.in);
        out.print("Enter dimensions:");
        length = sc.nextDouble();
        breadth = sc.nextDouble();
        height = sc.nextDouble();
    }
    void display()
    {
        double vol = length*breadth*height;
        out.println("Volume of the box: "+vol);
    }
}
class Area extends Box
{
  void display()
  {
      super.display();
      double ar = 2 * (length*breadth + breadth*height + height * length);
      out.println("Area of the box: "+ar+"square units");
  }
}
public class BoxDemo2
{
    public static void main(String args[])
    {
        Box a = new Box();
        Box b = new Area();
        out.println("For A");
        a.input();
        out.println("For B");
        b.input();
        out.println("A");
        a.display();
        out.println("B");
        b.display();
    }
}
