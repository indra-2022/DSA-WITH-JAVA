package Encapsulation;

public class Example {    
   private int a=10;
   private int b=20; //They are private so we cant directly access them

    public int getA() {
        return a;
    }      // Thats why we have public method which are accessable,and it will
           // return the value
           
     public int getb(){
        return b;
    }
}
