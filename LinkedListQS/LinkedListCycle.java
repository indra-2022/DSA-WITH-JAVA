package LinkedListQS;
   // LeetCode qs, Number- 141
    // https://leetcode.com/problems/linked-list-cycle/description/
public class LinkedListCycle extends NodeCreation {
    public boolean IsCycle(){
    Node first = head;
    Node slow = head;
    while(first!=null&&first.next!=null)
    {
        first = first.next.next;
        slow = slow.next;
        if (first == slow) {
            return true;
        }
    }return false;
}
}

                     // LEETCODE VERSION CODE



//   Definition for singly-linked list.
//   class ListNode {
//      int val;
//      ListNode next;
//       ListNode(int x) {
//           val = x;
//           next = null;
//      }
//   }
//  
// public class Solution {
//     public boolean hasCycle(ListNode head) {
//         ListNode first = head;
//         ListNode slow = head;
//         while(first != null && first.next != null){
//             first=first.next.next;
//             slow=slow.next;
//             if(first==slow){
//                 return true;
//             }
//         }
//         return false;
//     }
// }


