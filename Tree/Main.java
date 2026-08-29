import java.util.Scanner;

public class Main {
    // See the hand notes for better explaination and implementation.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeIntro Tree = new TreeIntro();
        //Use true false to populate
        Tree.populate(sc);
        Tree.display();
    }
}
