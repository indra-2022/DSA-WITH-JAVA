import java.util.ArrayList;

public class Introduction {
   public static void main(String[] args) {
    try{
    int a=10;
    int b=0;
    System.out.println(a/b);
      //This code will give exception
      
   }catch(Exception e){
    System.out.println("Please check the entered values and do again");
    //Now this will not give any exception while running
    //This is just a basic example of Exception Hndeling
   }
}
}
