import java.util.*;
public class switc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER 1 OR 2 OR 3");
        int a=sc.nextInt();
        switch (a) {
            case 1:
                System.out.println("Hello");
                break;
            case 2:
                System.out.println("HOLA");
                break;
            case 3:
                System.out.println("FAHHH");
                break;
            default:
                break;
        }
    }
}
