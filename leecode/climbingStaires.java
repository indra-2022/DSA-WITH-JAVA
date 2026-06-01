//https://leetcode.com/problems/climbing-stairs/description/
public class climbingStaires {
    public static void main(String[] args) {
        System.out.println(climb(3));
     }
    static int climb(int n){
        if(n==1){
            return 1;
        }
       int[] stairs = new int[n+1];
       stairs[1]=1;
       stairs[2]=2;
       for(int i=3;i<=n;i++){
        stairs[i]=stairs[i-1]+stairs[i-2];
       }
       return stairs[n];
    }
}
/*The calculation is easy but tricky,what we have in the question is the step for
1 and 2,so bassically insteed of calculating all the steps for n num every time,we will
simply creates an array where we store the data. How -> if n=3, then we can say 1+2=3,just
like for n=5 we can say 4+3 and so on.
 */
