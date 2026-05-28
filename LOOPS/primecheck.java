import java.util.Scanner;

public class primecheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter num");
        int num=sc.nextInt();
        boolean prime=true;
        for(int i=2;i<num;i++){
            if (num%i==0) {
                prime = false;
            }
        }
        if (prime) {
            System.out.println("Prime");
        }
        else
        {
            System.out.println("Not prime");
        }
    }
}
