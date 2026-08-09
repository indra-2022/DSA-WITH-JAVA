package Linkedlist;

public class DMain {
    public static void main(String[] args) {
        Doubly list = new Doubly();
        list.DInsertFirst(20);
        list.DInsertFirst(10);
        list.DInsertLast(30);
        list.DInsertFirst(990);
        list.DInsertFirst(210);
        list.DInsertLast(320);
        // list.display();
        // list.DDeleteIndex(2);
        list.display();
        list.DisplayRev();
    }
}
