public class bs {
    public static void main(String[] args) {
        int[] arr = {
                2, 5, 7, 10, 13, 17, 19, 23, 27, 30,
                34, 38, 41, 45, 49, 52, 56, 60, 63, 67,
                71, 75, 78, 82, 85, 89, 93, 97, 100, 105,
                110, 115, 120, 125, 130, 135, 140, 145, 150, 155
        };

     System.out.println("The index is-->"+search(arr, 0, arr.length-1,150));
    }
    static int search(int[]arr,int start,int end,int target){
           int mid = start + (end - start) / 2;
           if (start > end ) {
                return -1;         // If no value found return -1
            }
           if (arr[mid]== target) {
                return mid;
           }
           else if (target < arr[mid]) {
                return search(arr, start, mid-1, target);
            }
            else{
              return search(arr, mid+1, end, target);
            }
}
}
