// 367. Valid Perfect Square->https://leetcode.com/problems/valid-perfect-square/description/
// Solved
// Easy
// Topics
// premium lock icon
// Companies
// Given a positive integer num, return true if num is a perfect square or false otherwise.

// A perfect square is an integer that is the square of an integer.
//  In other words, it is the product of some integer with itself.
// You must not use any built-in library function, such as sqrt.
// Example 1:
// Input: num = 16
// Output: true
// Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

public class findValidSQRT {
    
    public boolean isPerfectSquare(int num) {
        if(num==1 || num==4 || num==9){
            return true;
        }
        for(int i=0;i<=num/4;i++){
            if(i*i==num){
                return true;
            }
        }
        return false;
    }
}



