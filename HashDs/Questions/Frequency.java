package HashDs.Questions;

import java.util.HashMap;

public class Frequency {
   public static void main(String[] args) {
     String[] fruits = {"apple", "banana", "apple", "orange", "banana", "apple"};
     HashMap<String,Integer> map = new HashMap<>();
     for(String fruit : fruits){
           map.put(fruit, map.getOrDefault(fruit, 0)+1);
     }
     System.out.println(map);
   }
}
