package LinkedListQS;

public class Middle extends NodeCreation {

    public void GetMiddle() {
        Node fast = head;
        Node slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        System.out.println("The middle of the list is->" + slow.value);

    }
}
