package Banking;

public class Account {
    private int Balance=0;
    private final int ActNo;
    private String name;
    private int pin;
    Account(String name,int pin){
     this.name=name;
      ActNo=(int)(Math.random()*900000)+100000;
      this.pin=pin;
    }
    public int getBalance() {
        return Balance;
    }
    public void DepositeBalance(int pin,int amt){
         if (pin ==this.pin) {
            Balance=Balance+amt;
            System.out.println("Balance is updated, New balance is "+ Balance);
         }
         else{
            System.out.println("WRONG PIN !!!!");
         }
    }
    public void Withdraw(int pin,int amt){
         if (pin ==this.pin) {
            if (Balance<amt) {
                System.out.println("low Balance");
            }
            else{
            Balance=Balance-amt;
            System.out.println("Balance is updated, New balance is "+ Balance);
            }
         }
         else{
            System.out.println("WRONG PIN !!!!");
         }
    }
    public int getActNo() {
        return ActNo;
    }
    public String getName() {
        return name;
    } 

}
