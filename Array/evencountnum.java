//1295. Find Numbers with Even Number of Digits
//https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
public class evencountnum {
    public static void main(String[] args) {
        int[]arr={1,22,344,56776,22,33,445,1,99876651};
        System.out.println(count(arr));
    }
    static int count(int arr[]){ 
        int count=0;
         for(int num:arr){
            if(even(num)==true){
               count++;
            }
         }
         return count;
    }
    static boolean even(int num){
        int count=0;
        while (num>0) {
            count++;
            num=num/10;
        }
        if(count%2==0){
            return true;
        }
        else{
            return false;
        }
    }
}
