//Find First and Last Position of Element in Sorted Array
//Input: nums = [5,7,7,7,7,8,8,10], target = 7
// Output: [1,4]

import java.util.Arrays;
public class firstLast {
    
public static void main(String[] args) {
    int[] nums = {5,7,7,7,7,8,8,10};
    int target=7;
        int[] result = searchRange(nums, target);
        System.out.println(Arrays.toString(result));
}
 static int[] searchRange(int[] nums, int target) {
        int[] ans={-1,-1};
        int start=search(nums,target,true);
        int end= search(nums, target, false);
        ans[0]=start;
        ans[1]=end;
        return ans;
    }
   static int search(int[]nums,int target,boolean findindex){
        int ans=-1;
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
        int mid = start + (end - start) / 2; // start+mid/2---> is the same
            if (target > nums[mid]) {
                start = mid + 1;
            }
            else if (target < nums[mid]) {
                end = mid - 1;
            }
            else{
                ans=mid;
                if(findindex==true){
                    end=mid-1;
                }
                else{
                    start=mid+1;
                }
            }
        }
        return ans;
    }
}

