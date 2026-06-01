import java.util.*;
public class intro {
    static void add(int a,int b){
           int c= a+b;
           System.out.println(c);
    }
    static void add(int a,int b,int d){
           int c= a+b+d;
           System.out.println(c);
                                             //This is called method over loading 
    }
   public static void main(String[] args) {
          add(5,6);
          add(10, 020, 022);
   }
}
