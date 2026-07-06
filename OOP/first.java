
public class first {
public static void main(String[] args) {
    Student indra = new Student(); // Created an obj
    indra.roll=45;  // Initialised it
    System.out.println(indra.roll);  // Print it
    indra.name="Indranil Ganguly";
    System.out.println(indra.name);

// All of this steps are repetetive so we can put the data in one,using a constructer

 Student indranil = new Student(450,"Indranil",77.0);
 System.out.println(indranil.roll);
 System.out.println(indranil.marks);

 //In this way we dont need to write indranil.marks=77.0 separetly
 // The initialisation is done with declaration it self

}
}
class Student{
    int roll;
    String name;
    double marks;

   Student(){

   }
    Student (int roll,String name,double number){
        this.roll=roll;
        this.name=name; // this keyword helps us when both the name is same,like the
                        // constructer and also the perameters
        marks=number; //---> but if not same we can use 2 different names eaasily
    }
}

