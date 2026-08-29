import java.util.Scanner;

public class Main {
    // See the hand notes for better explaination and implementation.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    //     TreeIntro Tree = new TreeIntro();
    //     //Use true false to populate
    //     Tree.populate(sc);
    //     Tree.display();
      BST bst = new BST();
      bst.Insert(10);
      bst.Insert(12);
      bst.Insert(15);
      bst.Insert(8);
      bst.Insert(20);
      System.out.println(bst.IsEmpty());
      bst.display();
      bst.GetHeight(null);
     }
}
