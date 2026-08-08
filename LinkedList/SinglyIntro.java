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
  private class Node { 
    private int value;
    private Node next;
    public Node(int value) {
      this.value = value;
    } 

    // public Node(int value, Node next) {
    //   this.value = value;
    //   this.next = next;
    // }
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

                    // DELETATION PART

                    // Delete the first index data
public void DeleteFirst(){
  head=head.next;
}
                   // Delete last Indext Data
public void DeleteLast(){
  if (head== null) {
    return;
  }
  Node temp = head;
   for(int i=0;i<size-2;i++){
      temp=temp.next;
   }
   tail=temp;
   tail.next=null;
   size--;
}
                // Delete at any index
public void DeleteIndex(int index){
  Node temp = head;
   for(int i=0;i<index-2;i++){
      temp=temp.next; //-> Pointing to previous element of the index
   }
   Node ex = temp.next; // Pointing to index
   temp.next=ex.next;
   size--;
   System.out.println(ex.value+"<-Is deleted");
}

                // Function to display data
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

                       //Function to get the size
public void GetSize(){
  System.out.println("The size of the LinkedList is--->"+ size);
}

  
}
