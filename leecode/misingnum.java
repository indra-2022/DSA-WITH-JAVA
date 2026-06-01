// Given an array nums containing n distinct numbers in the range [0, n]
// return the only number in the range that is missing from the array.
// Example 1:
// Input: nums = [3,0,1]
// Output: 2
// Explanation:
// n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
// 2 is the missing number in the range since it does not appear in nums.
//https://leetcode.com/problems/missing-number/description/

import java.util.Arrays;

public class misingnum {
    public static void main(String[] args) {
        int[] arr = { 1, 3, 4, 2, 5, 6, 10, 9, 8 };
        int res=find(arr);
        System.err.println(Arrays.toString(arr));
        System.err.println(res);
    }

    static int find(int[] arr) {
        int i = 0;
        while (i < arr.length) {
            if (arr[i] < arr.length && arr[i] != arr[arr[i]]) {
                swap(arr, i, arr[i]);
            } else {
                i++;
            }
        }
        for (int j = 0; j < arr.length; j++) {
            if (arr[j] != j) {
                return j;
            }
        }
        return arr.length;

    }

    static void swap(int[] arr, int first, int second) {
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }

}
