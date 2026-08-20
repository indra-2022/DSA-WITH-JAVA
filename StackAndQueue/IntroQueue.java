package StackAndQueue;
import java.util.LinkedList;
import java.util.Queue;
public class IntroQueue {
   public static void main(String[] args) {
    Queue queue = new LinkedList<>();
    queue.add(10);
    queue.add(20);
    queue.add(30);
    queue.add(40);
    queue.add(50);
    System.out.println(queue.toString());
    System.out.println(queue.remove());
    System.out.println(queue.toString());
   }
}
