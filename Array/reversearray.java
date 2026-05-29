import java.util.Arrays;
public class reversearray {
    public static void main(String[] args) {
        int[] arr ={20,30,40,50,60};
        swap(arr);
    }
   static void swap(int arr[]){
         int len=arr.length;
        // System.out.println(len);
        int temp;
       int last=len-1;

        for(int i=0;i<(int)len/2;i++){
           temp=arr[i];
           arr[i]=arr[last];
            arr[last]=temp;
            last--;
        }
        System.out.print(Arrays.toString(arr));
    }
}
