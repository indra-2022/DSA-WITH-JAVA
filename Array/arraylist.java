import java.util.ArrayList;

public class arraylist {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        list.add(10);
        list.add(1670);
        list.add(5610); // In arraylist we can store multipple data in an array
        list.add(125440); // withoout decleraing the data size while initializing
        list.add(125440);
        list.add(1450);
        list.add(14510);
        list.add(1240);
        list.add(10);
        System.out.println(list);
        System.out.println("IS the element is present?_> "+list.contains(1450));
        int a=list.indexOf(1450);
        System.out.println("The elemennt "+list.remove(a)+" Is removed");
        System.out.println(list);
    }
}
