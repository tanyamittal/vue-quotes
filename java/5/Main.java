
abstract class Base {
    Base()
    {
        System.out.println("Abstract classes can have constructors.");
    }
    abstract void fun();
    void joy()
    {
        System.out.println("You can have non abstract functions in abstract classes too.");
    }
}
final class Derived extends Base {
    Derived(){
        System.out.println("This class can not be derived further");
    }
    void fun() { System.out.println("Derived fun() called"); }
}

// class NonExistent extends Derived{} 

class Main {
    public static void main(String args[]) {

        // Uncommenting the following line will cause compiler error as the
        // line tries to create an instance of abstract class.
        // Base a = new Base();

        // We can have references of Base type.
        Base b = new Derived();
        b.fun();
        b.joy();
    }
}
