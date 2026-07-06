// We will have to findan element inside an infinite array
// (infinite=we dont know the size of the array and we cant use length())
public class posinfin {
    public static void main(String[] args) {
        int[] exp={10,20,34,54,65,76,87,89,91,95,97,100};
        int target=91;
        System.out.println(ans(exp, target));
    }
   static int ans(int[] arr,int target){
      int start=0;
      int end =1;
      while (target>arr[end]) {
       int newstart=end+1;
        end=end+(end-start+1)*2;
        start=newstart;
      }
      return getvalue(arr, target, start, end);
   }
    static int getvalue(int[] arr,int target,int start,int end){
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
}  // This code wil not run here,bcs technically its not a infinite array
  // The code was successfully tested on original platform and it was running perfectly
