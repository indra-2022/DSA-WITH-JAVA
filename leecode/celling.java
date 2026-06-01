//Just like a basic binary serach,but if the num is not found it will return the larger element next to it
public class celling {
    public static void main(String[] args) {
        int[] arr = {10,15,17,20,25,27,30};
     int target=26;
    int res=cellling(arr, target);
    System.out.println(arr[res]);
 }
    static int cellling(int arr[], int target) {
         if (target > arr[arr.length - 1]) {
            return -1; // Target is greater than the largest element in the array
         }
        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
        int mid = start + (end - start) / 2; // start+mid/2---> is the same
            if (target > arr[mid]) {
                start = mid + 1;
            }
            else if (target < arr[mid]) {
                end = mid - 1;
            }
            else{
                return mid;
            }
        }
        return start;
    }
}
