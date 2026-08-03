public class intro {
    public static void main(String[] args) {
        int[] arr= {1,2,3,4,4,5,6};
           int x=arr.length;
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i ]);
        }
        
    }
    /* Java arrays are not guaranteed to be stored in contiguous memoryn Why?
    Because Java never gives direct access to memory addresses.
    The JVM is free to manage memory however it wants. */
}
