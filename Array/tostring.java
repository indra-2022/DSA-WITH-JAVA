import java.util.Arrays;
import java.util.Scanner;

public class tostring {
     public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the size");
        int n=sc.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println(Arrays.toString(arr)); // Print using to String
         for(int num:arr){
                  System.out.println(num);   //Print using for each loop
         }
}
}
