import java.util.Arrays;

public class binarysearchfullsorted {
    public static void main(String[] args) {
        int[][] arr = {
    {1,  3,  5,  7},
    {10, 11, 16, 20},
    {23, 30, 34, 60},
    {65, 70, 75, 80}
};
   int target =16;
   System.out.println(Arrays.toString(search(arr, target)));
  
    }
    static int[] search(int[][] arr,int target){
             int row=arr.length;
             int col= arr[0].length;
             int start=0; 
             int end = row*col-1;
          
    }

    
}
