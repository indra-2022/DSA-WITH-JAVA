public class specialcase {
    public static void main(String[] args) {
        System.out.println(num(5));
    }
    static int num(int n){
        if (n==0) {
            return 0;
        }
        System.out.println(n);
        //return num(n--);  // It might look it will print 5,4,3,2,1,0 but not
                          // n is calling before its decreasing so n never becomes 4,3,2,1,0
                          // Insteed of (n--) Do (--n)
        return num (--n); // Like this
    }
}
