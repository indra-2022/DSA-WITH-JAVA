public class removeDup {
  public static void main(String[] args) {
    int []arr={1,2,3,4,8,9,5,0,4,7,3,8,9,1};
    int[]arr2= new int[arr.length];
    int count=0;
    boolean isduplicate=false;
    for(int i=0;i<arr.length;i++){
        for(int j=0;j<=count;j++){
            if(arr[i]==arr2[j]){
                isduplicate=true;
                break;
            }
        }
        if (!isduplicate) {
            arr2[count]=arr[i];
            count++;
        }
    }
    for(int k=0;k<count;k++){
        System.out.print(arr2[k]+" ");
    }
  }
    
}
