import java.util.Scanner;

public class pattern6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter row");
        int row = sc.nextInt();
        System.out.println("Enter column");
        int col = sc.nextInt();
        int ch = 65;
        for (int i = 1; i <= row; i++) {
            if (i % 2 == 0) {
                for (int j = 0; j < col; j++) {
                     System.out.print((char)(ch + 32) + " ");
                }
            } else {
                for (int j = 0; j < col; j++) {
                    System.out.print((char)(ch) + " ");
                }
            }
            ch++;
            System.out.println();
        }
    }

}