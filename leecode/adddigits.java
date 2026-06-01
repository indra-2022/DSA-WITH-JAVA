//https://leetcode.com/problems/add-digits/
// Given an integer num
// repeatedly add all its digits until the result has only one digit, and return it.
// Example 1:
// Input: num = 38
// Output: 2
// Explanation: The process is
// 38 --> 3 + 8 --> 11
// 11 --> 1 + 1 --> 2 
// Since 2 has only one digit, return it.

public class adddigits {
    public static void main(String[] args) {
        System.out.println(addDigits(38));
    }
    static int addDigits(int n) {
        if(n<10){
            return n;
        }
        int sum=0;
        while(n!=0){
        int num=n%10;
        sum=sum+num;
        n=n/10;
        }
        return addDigits(sum);
    }
}


