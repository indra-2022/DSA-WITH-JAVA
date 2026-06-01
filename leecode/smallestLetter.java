/*  Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character 
that is lexicographically greater than 'a' in letters is 'c'. */
//https://leetcode.com/problems/find-smallest-letters-greater-than-target/description/
public class smallestLetter {
    
 public static void main(String[] args) {
    char[] letters={'a','b','d','f','k','m','s'};
    char target='e';
    System.out.println(nextGreatestLetter(letters,target));

 }
    
 static char nextGreatestLetter(char[] letters, char target) {
        int start = 0;
        int end = letters.length - 1;
        while (start <= end) {
        int mid = start + (end - start) / 2;
            if (target >= letters[mid]) {
                start = mid + 1;
            }
            else{
                end=mid-1;
            }   
        }
       return letters[start % letters.length];
    }
}

