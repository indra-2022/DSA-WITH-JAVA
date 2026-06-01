public class revers {
      static int reverse=0;
    static void rev(int n){
        if(n==0){
            return;
        }
        int num=n%10;
       reverse=reverse*10+num;
         rev(n/10);
    }
    public static void main(String[] args) {
        rev(1234);
        System.out.println(reverse);
    }
   
}
