public class zerocounter {
   static int counter=0;
    public static void main(String[] args) {
        counter(40002);
        System.out.println(counter);
    }
   static int counter(int n){
    if (n==0) {
        return 1;
    }
     if(n%10==0) {
          counter++;
       }
       return counter(n/10);
   }
}
