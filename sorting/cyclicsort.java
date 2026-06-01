import java.util.Arrays;

public class cyclicsort {
    public static void main(String[] args) {
        try {
            int[] arr = { 1, 3, 4, 2, 5, 6, 10, 9, 8, 7 };
            cyclic(arr);
            System.err.println(Arrays.toString(arr));

        } catch (Exception e) {
            System.err.println("This array is not suitable for Cyclic sort because-> " + e.getMessage());
        }
    }

    static void cyclic(int[] arr) {
        int i = 0;

        while (i < arr.length) {
            int index = arr[i] - 1;

            if (arr[i] != arr[index]) {
                swap(arr, i, index);
            } else {
                i++;
            }
        }
    }

    static void swap(int[] arr, int first, int second) {
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}
