public class Square extends Shaapes {
   void area(){
    System.out.println("I am from Square class");
   }

    // Here we are doing Method overloading,same name of the methods but with different
    //parameters/Return type/value so java will automatically chose the correct one 
   void area(int a){
    System.out.println("I am from Square class with a value of "+a);
   }


   void area(int a, int b){
    System.out.println("I am from Square class with value of a "+a+" and b "+ b);
   }


//    Square(){
//     super.area();
//    } //Working of parent using super


}
