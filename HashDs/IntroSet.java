package HashDs;

import java.util.HashSet;

public class IntroSet {
    public static void main(String[] args) {
        HashSet<Integer> obj = new HashSet<>();
        obj.add(10);
        obj.add(11);
        obj.add(10);
        System.out.println(obj);
    }
}
