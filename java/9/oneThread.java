public class oneThread extends Thread {
    public void run()
    {
        System.out.println("Hello ");
        try {
            Thread.sleep(300);
        }
        catch (InterruptedException ie) {
        }
        System.out.println("Java ");
    }
    public static void main(String[] args)
    {
        oneThread c1 = new oneThread();
        oneThread c2 = new oneThread();
        System.out.println(c1.getPriority());
        System.out.println(c2.getPriority());
        c1.setPriority(1);
        c2.setPriority(10);
        c1.start();
        try {
            c1.join(); // Waiting for c1 to finish
        }
        catch (InterruptedException ie) {
        }

        c2.start();
        System.out.println(c1.isAlive());
        System.out.println(c2.isAlive());
    }
}
