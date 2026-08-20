package Stack;

import java.util.Stack;

public class Introduction {
   public static void main(String[] args) {
    Stack<Integer> stack = new Stack<>();
    stack.push(10);
    stack.push(20);
    stack.push(30);  // In built methods for stack push
    stack.push(40);
    stack.push(50);
    System.out.println(stack.toString()); //To dispplay we are comverting it to String
      System.out.println(stack.pop()+" Is Deleted");
      //The pop method internally returns ṭhe data its deleted
      //  so we can just print the data using sout
      System.out.println(stack.toString());
   }
}
