package LinkedListQS;

public class RemoveDuplicate extends NodeCreation {
    public void Removedup(){
        Node pointer = head;
        while (pointer.next != null) {
            if (pointer.value == pointer.next.value) {
                pointer.next=pointer.next.next;
            }
        }
    }
}
