//This is not for fully sorted array,it for row and columns wise sorted array
import java.util.Arrays;

public class binarysearch2d {
    public static void main(String[] args) {
        int[][] arr = {
    {10, 20, 30, 40},
    {15, 25, 35, 45},
    {28, 29, 37, 49},
    {33, 34, 38, 50}
};
int target=37;
  System.out.println(Arrays.toString(search(arr, target)));
    }
    static int[] search(int[][] arr,int target){
        int row=0;
        int col=arr.length-1;
        while (row<arr.length && col>=0) {
            if (target== arr[row][col]) {
                return new int[]{row,col};
            }
            if (target>arr[row][col]) {
                row++;
            }
            else{
                col--;
            }
        }
        return new int[]{-1,-1};

    }
}
