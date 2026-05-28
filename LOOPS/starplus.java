import java.util.*;

public class starplus {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Row and Col must be odd");
        System.out.println("Enter row");
        int row = sc.nextInt();
        System.out.println("Enter column");
        int col = sc.nextInt();
        int mid=col/2+1;
        for(int i=1;i<=row;i++){
            for(int j=1;j<=col;j++){
                if(i==mid || j==mid){
                    System.out.print("*");
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
