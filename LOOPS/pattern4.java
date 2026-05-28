import java.util.*;
public class pattern4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter row");
        int row=sc.nextInt();
        System.out.println("Enter column");
        int col=sc.nextInt();

        for(int i=0;i<row;i++){
            for(int j=1;j<=col;j++){
                System.out.print((char)(j+64)+" "); 
            }
            System.out.println();
        }
    }
}
