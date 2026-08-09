package Linkedlist;

public class Doubly {
    private Node head;
    private Node tail;
    private int size;
    private Node prev;

    public Doubly() {
        this.size = 0;
    }

    private class Node {
        private int value;
        private Node next;
        private Node prev;

        public Node(int value) {
            this.value = value;
        }
    }

    public void DInsertFirst(int val) {
        Node node = new Node(val);
        if (head == null) {
            head = node;
            tail = node;
        } else {
            node.next = head;
            head.prev = node;
            head = node;
        }
        size++;
    }

    public void DInsertLast(int val) {
        if (tail == null) {
            DInsertFirst(val);
            return; // Check if the list is emepty then just call the InsertFirst method
        }
        Node node = new Node(val);
        tail.next = node;
        node.prev = tail;
        tail = node;
        node.next = null;
        size++;
    }

    public void InsertAtIndex(int val, int index) {
        if (index == 0) {
            DInsertFirst(val);
            return;
        }

        if (index == size) {
            DInsertLast(val);
            return;
        }

        Node temp = head;
        for (int i = 0; i < index - 1; i++) {
            temp = temp.next;
        }
        Node ex = temp.next;
        Node node = new Node(val);
        node.next = temp.next;
        ex.prev = node;
        temp.next = node;
        node.prev = temp;
        size++;
    }
    // DELETING PART

    // public void DdeleteIndex(int index){
    // Node temp = head;
    // for(int i=0;i<index-2;i++){
    // temp=temp.next; //-> Pointing to previous element of the index
    // }
    // Node ex = temp.next; // Pointing to index
    // Node nxt = ex.next;
    // temp.next=ex.next;
    // nxt.prev = temp;
    // size--;
    // System.out.println(ex.value+" Is deleted");
    // }

    public void DDeleteIndex(int index) {
        Node temp = head;
        for (int i = 1; i < index - 1; i++) {
            temp = temp.next;
        }
        temp.next = temp.next.next;
        temp.next.prev = temp;
        size--;
    }

    public void display() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.value + "->");
            temp = temp.next;
            if (temp == null) {
                System.out.print("End");
            }
        }
        System.out.println();
    }

    public void DisplayRev() {
        Node temp = tail;
        while (temp != null) {
            System.out.print(temp.value + "<-");
            temp = temp.prev;
            if (temp == null) {
                System.out.print("Start");
            }
        }
        System.out.println();
    }
}
