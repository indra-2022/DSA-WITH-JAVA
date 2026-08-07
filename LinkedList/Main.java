package Linkedlist;

import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
       SinglyIntro list = new SinglyIntro();
    //    list.InsertFirst(100);
    //    list.InsertFirst(90);
    //    list.InsertFirst(80);  // Self define methods for linkedlist 
          list.InsertFirst(70);
          list.InsertLast(80);
          list.InsertLast(90);  // Using Self define method
          list.InsertAtIndex(85, 2);
          list.display();
         //LinkedList<Integer> list = new LinkedList<>();
        // list.add(90); -> [Using Internal Implementations]
        // System.out.println(list.get(0));

    }
}
