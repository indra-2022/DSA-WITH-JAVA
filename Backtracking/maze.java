//Finding all the possible combination for the path 
// This code might looks messy and not understable,and very easy but the thinkin and the 
// algo behind it is very logical,written on physical note
public class maze {
    public static void main(String[] args) {
        System.out.println(finder(3, 3));
    }
    static int finder(int r, int c) {
        if (r == 1 || c == 1) {
            return 1;
        }
        int left = finder(r - 1, c);
        int right = finder(r, c - 1);
        return left + right;
    }
}
// (3,3) is index of 2d array,and 6 is the ans of -->"How many ways are there to reach (1,1)"
// we can only go [Right Or Left] 
