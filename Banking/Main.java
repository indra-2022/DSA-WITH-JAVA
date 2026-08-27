package Banking;

public class Main {
  public static void main(String[] args) {
    Account obj = new Account("Indranil Ganguly",0000);
    System.out.println(obj.getActNo());
    System.out.println(obj.getName());
    obj.DepositeBalance(0000, 100000000);
    obj.Withdraw(0000, 1000);
  }
}
