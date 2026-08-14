package LinkedListQS;

public class MergeSorted extends NodeCreation {

    public static void Merge(NodeCreation List1,NodeCreation List2){
             Node first = List1.head;
             Node second = List2.head;
             NodeCreation ans = new NodeCreation();
             while (first!= null && second != null) {
                if (first.value < second.value) {
                    ans.InsertLast(first.value);
                    first=first.next;
                }
                else{
                    ans.InsertLast(second.value);
                    second=second.next;
                }
                while (first != null) {
                    ans.InsertLast(first.value);
                    first=first.next;
                }
                while (second != null) {
                    ans.InsertLast(second.value);
                    second=second.next;
                }
             }
             ans.display();
}
// Fking complicated Implementation
}
