public class numTozero {
    static int counter=0;
    public static void main(String[] args) {
        count(14);
        System.out.println(counter);
    }
    static void count(int n){
        if(n==0){
            return;
        }
        if (n%2==0) {
            counter++;
            count(n/2);
        }
        else{
            counter++;
            count(n-1);
        }
    }
}
