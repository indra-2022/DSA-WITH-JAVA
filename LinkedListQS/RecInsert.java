// Rescursive inserion in an LinkedList
package LinkedListQS;
public class RecInsert extends NodeCreation{

public void insert(int val, int index) {
    head = insert(val, index, head);
    size++;
}

private Node insert(int val, int index, Node node) {
    if (index == 0) {
        Node temp = new Node(val);
        temp.next = node;
        return temp;
    }

    node.next = insert(val, index - 1, node.next);
    return node;
}
}
