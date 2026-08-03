package Linkedlist;
import java.util.LinkedList;
//In traditional way Linkedlist need to a have pointer to implement like we do in [c/c++]
// but here in java we dont have pointers then how will we implement it? 
//Java does have pointers internally it just doesn't let programmers use them directly
// Instead Java gives you references

public class SinglyIntro {
  private Node head;
  private Node tail;
  private int size;
  
  public SinglyIntro() {
    this.size = 0;
  }

public void InsertfIRST(int val){ // Function to add data at first position
  Node node = new Node(val);
  node.next=head;
  head=node;
  if (tail==null) {
      tail=head;
  }
}

public void display(){ // Function to display data
  Node temp = head;
  while (temp!= null) {
    System.out.println(temp.value);
    temp=temp.next;
  }
}

  private class Node {
    private int value;
    public Node(int value) {
      this.value = value;
    }
    public Node(int value, Node next) {
      this.value = value;
      this.next = next;
    }
    private Node next;
  }
}
