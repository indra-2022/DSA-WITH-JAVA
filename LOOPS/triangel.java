import java.util.*;
public class triangel {
     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter row");
        int row = sc.nextInt();
        System.out.println("Enter column");
        int col = sc.nextInt();
        for(int i=1;i<=row;i++){
            
             for(int j=row;j>i;j--){
                    System.out.print(" ");
             }
            for(int k=1;k<=i;k++){
                System.out.print("* ");
            }

            System.out.println();
        }
    }
}
