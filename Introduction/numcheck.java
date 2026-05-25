import java.util.*;

class numcheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter data for A and B");
        int a = sc.nextInt();
        int b = sc.nextInt();
        sc.close();
        int sum = a + b;
        if (sum > 0) {
            System.out.println("Is posetive");

        } else {
            System.err.println("Sum is negetive");
        }
        if (sum % 2 == 0) {
            System.out.println("Sum is even num");

        } else {
            System.out.println("Sum is odd num");
        }
    }

}