package Encapsulation;

public class Main {
   public static void main(String[] args) {
    Example obj = new Example();
    //System.out.println(obj.a);->We cant access a bcs its private
    System.out.println(obj.geta()); //It will give us data of a
    System.out.println(obj.getb()); // It will give us data of b
    
   }
}
