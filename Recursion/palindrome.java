public class palindrome {
    static int reverse=0;
    public static void main(String[] args) {
        System.out.println(pali(121));
    }
    static boolean pali(int n){
        rev(n);
        if (n==reverse) {
            return true;
        }
        else{
            return false;
        }
        
    }
    static void rev(int n){
        if(n==0){
            return;
        }
        int num=n%10;
       reverse=reverse*10+num;
         rev(n/10);
    }
}
