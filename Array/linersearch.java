import java.util.Arrays;
import java.util.Scanner;

public class linersearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter num here-->");
        int num = sc.nextInt();
        int[] arr = {
                -50, -40, -30, -20, -10,
                -5, -2, 0, 3, 7,
                10, 15, 20, 25, 30,
                35, 40, 45, 50, 55,
                60, 65, 70, 75, 80,
                85, 90, 95, 100, 110
        };
        //Arrays.sort(arr);
        search(arr, num);
    }

    static void search(int arr[], int num) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == num) {
                System.out.println("The num " + num + " Is found and the index is " + i);
                break;
            }
        }
        System.out.println("Num not found");
    }
}
