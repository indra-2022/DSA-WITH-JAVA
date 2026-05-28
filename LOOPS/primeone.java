import java.util.Scanner;

public class primeone {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Range");
        int num = sc.nextInt();
        for (int i = 2; i <=num; i++) {
            boolean prime = true;
            for (int j = 2; j<i; j++) {   
                if (i % j == 0) {
                    prime = false;
                    break;
                }
            }
            if (prime) {
                System.out.println(i);
            }
        }
    }
}
