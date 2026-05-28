import java.util.*;
public class pattern5 {
    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
        System.out.println("Enter row");
        int row=sc.nextInt();
        System.out.println("Enter column");
        int col=sc.nextInt();
        int printer=1;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                System.out.print(printer+" ");
            }
            printer++;
            System.out.println();
        }
    }
}
