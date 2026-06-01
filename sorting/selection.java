import java.util.Arrays;

public class selection {
    public static void main(String[] args) {
        int[] arr = { 2, 5, 1, 3, 4 };
        System.out.println(Arrays.toString(arr));
        selectionsort(arr);
        System.out.println(Arrays.toString(arr));
    }

    static void selectionsort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int last = arr.length - i - 1;
            int max = maxfinder.findmax(arr, 0, last);
            int temp = arr[last];
            arr[last] = arr[max];
            arr[max] = temp;
        }
    } // This is selection sort algo,here we are finding the max element that is not
      // written in this code for that we have ceated a separate class and using this
}

class maxfinder {
    static int findmax(int[] arr, int first, int last) {
        int max = first;
        for (int i = first; i <= last; i++) {
            if (arr[max] < arr[i]) {
                max = i;
            }
        }
        return max;
    }
}
// Selection Sort can also work by finding the largest/smallest element
// and placing it at the end in each step.
// 👉 Mini example:
// Array: [4, 2, 1, 5]
// Step 1: largest = 5 → already at end
// Step 2: largest = 4 → swap with 1 → [1, 2, 4, 5]
// Step 3: largest = 2 → already correct ✅