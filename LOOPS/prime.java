import java.util.Scanner;
public class prime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Range");
        int num=sc.nextInt();
       for(int i=2;i<num;i++){
        isprime(i);
       }
    }
    static void isprime(int num){
           boolean prime=true;
        for(int i=2;i<num;i++){
            if (num%i==0) {
                prime = false;
            }
        }
        if (prime) {
            System.out.println(num);
        }
    }
}
