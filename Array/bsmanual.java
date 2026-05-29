public class bsmanual {
    public static void main(String[] args) {
        int[] arr = {
    2, 5, 7, 10, 13, 17, 19, 23, 27, 30,
    34, 38, 41, 45, 49, 52, 56, 60, 63, 67,
    71, 75, 78, 82, 85, 89, 93, 97, 100, 105,
    110, 115, 120, 125, 130, 135, 140, 145, 150, 155
};
        int target=89;
        if(arr[0]<arr[arr.length-1]){
            System.out.println(bsasc(arr, target));
        }  // TO CHECK WEATHER THE ARRAY IS IN AS WHICH ORDER 
        else{
            System.out.println(bsdes(arr, target));
        }
    }

    static int bsasc(int arr[], int target) {

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
        return -1;
    }
    static int bsdes(int arr[], int target) {

        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
        int mid = start + (end - start) / 2; // start+mid/2---> is the same
            if (target > arr[mid]) {
                
                end = mid - 1;
            }
            else if (target < arr[mid]) {
                start = mid + 1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
}
