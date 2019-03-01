import java.util.StringTokenizer;
public class strtkn
{
    public static void main(String args[])
    {
        StringTokenizer st = new StringTokenizer("This is an example of StringTokenizer class");
        System.out.println("Number of tokens in the given string is: "+st.countTokens());
        while(st.hasMoreElements()){
            System.out.println(st.nextElement());
        }
        StringTokenizer str = new StringTokenizer("This,is,an,example,of,StringTokenizer,class,based,on,delimeter");
        while(str.hasMoreTokens()){
            System.out.println(str.nextToken(","));
        }

    }
}
