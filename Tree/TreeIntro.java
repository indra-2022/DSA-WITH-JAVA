import java.util.Scanner;

public class TreeIntro {

    public TreeIntro() {

    }

    private static class Node {
        int value;
        Node left;
        Node Right;

        public Node(int value) {
            this.value = value;
        }
    }

    private Node root;

    public void populate(Scanner sc) {
        System.out.println("Enter the root Node: ");
        int value = sc.nextInt();
        root = new Node(value);
        populate(sc, root);
    }

    public void populate(Scanner sc, Node node) {
        System.out.println("Do u want to eneter left value of " + node.value);
        Boolean left = sc.nextBoolean();
        if (left) {
            System.out.println("Enter the value");
            int val = sc.nextInt();
            node.left = new Node(val);
            populate(sc, node.left);
        }
        System.out.println("Do you want to enter Right of " + node.value);
        boolean Right = sc.nextBoolean();
        if (Right) {
            System.out.println("Enter the value of the Right of " + node.value);
            int value = sc.nextInt();
            node.Right = new Node(value);
            populate(sc, node.Right); 
            
        }
    }
      public void display() {
    display(this.root, "");
  }
//Display Function 
  private void display(Node node, String indent) {
    if (node == null) {
      return;
    }
    System.out.println(indent + node.value);
    display(node.left, indent + "\t");
    display(node.Right, indent + "\t");
  }
   

// This is to display with good looks
   public void ADisplayDisplay() {
    ADisplayDisplay(root, 0);
  }

  private void ADisplayDisplay(Node node, int level) {
    if (node == null) {
      return;
    }

    ADisplayDisplay(node.Right, level + 1);

    if (level != 0) {
      for (int i = 0; i < level - 1; i++) {
        System.out.print("|\t\t");
      }
      System.out.println("|------->" + node.value);
    } else {
      System.out.println(node.value);
    }
    ADisplayDisplay(node.left, level + 1);
  }
}
