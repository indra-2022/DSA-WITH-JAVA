public class WrapperExample {
public static void main(String[] args) {
    int a =5; // Premeive DT
    int b= 10;
    Integer num1 =10; 
    Integer num2=20; //Object
    swap(a, b);
    System.out.println(a + "  " + b);  // The swapping is not done on the original 
    //veriable,bcs java send ref as parameter not actual value

    swapRef(num1, num2); // Here happening the same,even if the DT is object
    System.out.println(num1+ "  " + num2); // BCS Integer uses (final),which makes it
    //unchangeble

    //  final int ex=5;
    //  ex=33;  Its giving error,cs of final
}
static void swap(int a,int b){
    int temp =b;
     b=a;
    a= temp;
    System.out.println(a + "  " + b);
}
static void swapRef(Integer a,Integer b){
    int temp =b;
     b=a;
    a= temp;
    System.out.println(a + "  " + b);
}
 
}