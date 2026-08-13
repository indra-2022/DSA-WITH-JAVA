package LinkedListQS;

public class NodeCreation {
public Node head;
  public Node tail;
  public int size;
  
  public NodeCreation() {
    this.size = 0;
  }
  public class Node { 
    public int value;
    public Node next;
    public Node(int value) {
      this.value = value;
    }
    
    public Node(int value, Node next) {
        this.value = value;
        this.next = next;
    }
    
}
}
