package AccessModifier;

public class main {
  public static void main(String[] args) {
    Demo obj = new Demo();
    //obj.a Error bcs a is private

    System.out.println(obj.b);//No error bcs b is public

    System.out.println(obj.getA());//But we can get data of [a] using getter
    System.out.println(obj.c); // The [c] is accessable bcs we are in the same package
    // Bcs [c] is default 
     System.out.println(obj.d); //Can be accessable
  }
}
