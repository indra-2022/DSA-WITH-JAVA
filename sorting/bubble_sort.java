import java.util.Arrays;
public class bubble_sort {
    public static void main(String[] args) {
       int[]arr={5,3,7,2,1};
       System.out.println(Arrays.toString(arr));
       bubble(arr);
       System.out.println(Arrays.toString(arr));
    }
    static void bubble(int[]arr){
          for(int i=0;i<arr.length;i++){
                 for(int j=1;j<arr.length-i;j++){
                    if (arr[j]<arr[j-1]) {
                        int temp= arr[j];
                        arr[j]=arr[j-1];
                        arr[j-1]=temp;
                    }
                 }
          }
    }
    
}
// Bubble Sort is a simple method where we repeatedly compare adjacent
//  elements and swap them if they are in the wrong order
//  so the largest elements slowly move to the end.
// 👉 Mini example:
// Array: [5, 3, 2]
// Step 1: compare 5 & 3 → swap → [3, 5, 2]
// Step 2: compare 5 & 2 → swap → [3, 2, 5]
// Step 3: compare 3 & 2 → swap → [2, 3, 5] ✅
