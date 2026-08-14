package LinkedListQS;

public class NodeCreation{
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
       //Just a basic Method to add data for Testing purposes
public void InsertFirst(int val){ 
  Node node = new Node(val);
  node.next=head;
  head=node;
  if (tail==null) {
      tail=head;
  }
  size++;
}

public void display(){ 
  Node temp = head;
  while (temp!= null) {
    System.out.print(temp.value+"->");
    temp=temp.next;
    if (temp==null) {
      System.out.print("End");
    }
  }
  System.out.println();
}

public void InsertLast(int val){
  if(tail==null){
    InsertFirst(val); 
    return; // Check if the list is emepty then just call the InsertFirst method
  }
  Node node = new Node(val);
  tail.next= node; 
  tail= node;
  size++;
}
}
