package HashDs.Questions;

import java.util.HashSet;

public class FoundDuplicate {
  public static void main(String[] args) {
    int [] arr = {1,2,3,4,5,6,1}; // we have 2 times [1],find that and print
    HashSet<Integer> set = new HashSet<>();
    for(int digit : arr){
        if (set.contains(digit)) {
            System.out.println(true+"->"+digit);
            return ;
        }
        else{
            set.add(digit);
        }
    }
  }
}
