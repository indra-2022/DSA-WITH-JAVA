public class Comparision {
    public static void main(String[] args) {
      //Ex1 Here both the ref variable is pointing to the same object that's holding
      //the value of "Indra",so technically in memory there is only one Indra
      //So its returning True
                 
        // String a = "Indra";
        // String b = "Indra";    
        // System.out.println(a == b);
 
        //But here we are telling java forget about yr optimisation create two diffrent 
        //Objects and store data,using (New) keyword,so its returning False

        // String name1=new String("abc");
        // String name2=new String("abc");
        // System.out.println(name1==name2);

        // (==)will check both the value and the refarenceif both are same then it wll
        // return True
        // Use .equals() to check only for value

        // String name1=new String("abc");
        // String name2=new String("abc");
        // System.out.println(name1.equals(name2));
    }
}
