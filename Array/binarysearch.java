import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class binarysearch {
    public static void main(String[] args) {
        int[] arr = {
    45, 12, 78, 3, 56,
    23, 89, 1, 67, 34,
    90, 11, 5, 72, 28,
    60, 19, 100, 2, 38
};
       Arrays.sort(arr);
       System.out.println(Arrays.toString(arr));
       Scanner sc = new Scanner(System.in);
        System.out.println("Enter num here-->");
        int num = sc.nextInt();
        System.out.println(Arrays.binarySearch(arr,num));
    }
}
