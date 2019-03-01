
// Java program to demonstrate working of
// interface.
//import java.io.*;

// A simple interface
interface in1
{
    // public, static and final
    final int a = 10;

    // public and abstract
    void display();
}

class baseClass implements in1
{
    public void display(){
        System.out.println("Implementing an interface in java");
    }

}
// A class that implements interface.
class testClass2 extends baseClass
{
    // Implementing the capabilities of
    // interface.
    public void display()
    {
        super.display();
        System.out.println("Extending an interface in java");
    }

    // Driver Code
    public static void main (String[] args)
    {
        testClass2 t = new testClass2();
        t.display();
        System.out.println(a);
    }
}
