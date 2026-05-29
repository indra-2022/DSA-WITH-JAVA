import java.util.Arrays;
public class movezero {   //Deloitte qs
    public static void main(String[] args) {
        int arr[] = { 1, 5, 6, 0, 2, 0, 8, 4, 0, 3, 0 };
        System.out.println(Arrays.toString(arr));
        remove(arr);
    }
    static void remove(int[] arr) {
        int[] arr2 = new int[arr.length];
        int count =0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i]!=0) {
                arr2[count]=arr[i];
                count++;
            }
        }
        System.out.println(Arrays.toString(arr2));
        // for(int j=0;j<count;j++){
        //     System.out.print(arr2[j]+" ");
        // }
    }
}
