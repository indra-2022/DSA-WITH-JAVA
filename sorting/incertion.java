import java.util.Arrays;

public class incertion {
      public static void main(String[] args) {
         int[] arr = { 2, 5, 1, 3, 4 };
        System.out.println(Arrays.toString(arr));
        insertion(arr);
        System.out.println(Arrays.toString(arr));
    }
    static void insertion(int[]arr){
           for(int i=0;i<arr.length-1;i++){
            for(int j=i+1;j>0;j--){
                if (arr[j]<arr[j-1]) {
                     int temp = arr[j];
                     arr[j] = arr[j-1];
                     arr[j-1] = temp;
                }else{
                    break;
                }
            }
           }
    }
}
// Insertion Sort is a method where we take one element at a 
// time and insert it into its correct position in the already sorted part of the array.
// Array: [5, 3, 4]
// Step 1: take 3, compare with 5 → insert before → [3, 5, 4]
// Step 2: take 4, place between 3 and 5 → [3, 4, 5] 
//Like arranging playing cards in your hand—you insert each card at the correct position.

