import myPackage.*;
class impPackage{
    public static void main(String args[])
    {
            myPackage.Class1 a = new myPackage.Class1();
            myPackage.Class2 b = new myPackage.Class2();
            myPackage.Class3 c = new myPackage.Class3();
            System.out.println("Importing package with all its classes");
            a.display();
            b.display();
            c.display();
    }
}
