package StackAndQueue;

import java.util.ArrayDeque;
import java.util.Deque;

public class IntroDeQueue {
    public static void main(String[] args) {
 Deque<Integer> obj = new ArrayDeque<>();
      obj.add(10);
      obj.addFirst(9);
      obj.addLast(15);
      System.out.println(obj);
      
 }
}
