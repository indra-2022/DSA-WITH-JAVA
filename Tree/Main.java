import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeIntro Tree = new TreeIntro();
        //Use true false to populate
        Tree.populate(sc);
        Tree.display();
    }
}
