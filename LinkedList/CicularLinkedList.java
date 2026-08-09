package Linkedlist;

public class CicularLinkedList {
    private int size;
    private Node head;
    private Node tail;

    private class Node {
       private int value;
       private Node next;
       public Node(int value) {
        this.value = value;
       }
    }
    public CicularLinkedList() {
          this.size=0;
    }

public void CInsertFirst(int val){ 
  Node node = new Node(val);
  node.next=head;
  head=node;
  if (tail==null) {
      tail=head;
  }
  tail.next=head;
  size++;
}
public void DisplayCirculer(){
    Node temp=head;
    while (temp.next!=head) {
       System.out.print(temp.value+"->");
    temp=temp.next;
    if (temp.next==head) {
      System.out.print("End");
    }
}
System.out.println();
}
    
}
