package HashDs.Questions;

import java.util.HashMap;

public class TwoSum {
    public static void main(String[] args) {
        int[] arr={1,2,3,4,5};
        twoSum(arr, 9);
    }
   
    public static void twoSum(int[] arr, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<arr.length;i++){
           int check= target - arr[i];
          if( map.containsKey(check)){
            // return new int[] {i,map.get(check)}; ----> Leetcode
            System.out.println(arr[i]+"+"+check+"="+target);
          }
          else{
            map.put(arr[i],i);
          }
        }
        // return new int[] {};
        
    }
}

