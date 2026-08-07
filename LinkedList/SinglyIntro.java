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
  private class Node { // This class is specially creating the node,bcs here we are writing everything 
    // From scratch 
    private int value;
    private Node next;
    public Node(int value) {
      this.value = value;
    } 
    public Node(int value, Node next) {
      this.value = value;
      this.next = next;
    }
    
  }

                      // Function to add data at first position
public void InsertFirst(int val){ 
  Node node = new Node(val);
  node.next=head;
  head=node;
  if (tail==null) {
      tail=head;
  }
  size++;
}

                    //Function to add node at last position
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

                // Function to Add Data at any index
public void InsertAtIndex(int val,int index){
if (index==0) {
  InsertFirst(val);
  return;
}

if (index==size) {
  InsertLast(val);
  return;
}

 Node temp = head;
 for(int i=0;i<index-1;i++){
    temp=temp.next;
 }
  Node node = new Node(val);
  node.next=temp.next;
  temp.next=node;
  size++;
}

                // Function to display data
public void display(){ 
  Node temp = head;
  while (temp!= null) {
    System.out.println(temp.value);
    temp=temp.next;
  }
}

                       //Function to get the size
public void GetSize(){
  System.out.println("The size of the LinkedList is--->"+ size);
}

  
}
