//https://www.geeksforgeeks.org/problems/replace-all-0s-with-5/1
// You are given an integer n. You need to convert all zeroes of n to 5.
// Examples:
// Input: n = 1004
// Output: 1554
// Explanation: There are two zeroes in 1004 on replacing all zeroes with 5
// the new number will be 1554.
public class replce0 {
    public static void main(String[] args) {
        System.out.println(convertfive(1004));
    }
   static int convertfive(int n) {
        int ans=0;
        int place=1;
        while(n!=0){
            int num=n%10;
            if(num==0){
                num=5;
            }
            ans=ans+(num*place);
            n=n/10;
            place=place*10;
        }
        return ans;
    }
}
